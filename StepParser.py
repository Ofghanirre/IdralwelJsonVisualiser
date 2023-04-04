example = {
    "id": "",
    "conditions": [
        ""
    ],
    "responses": [
        {
            "id": "",
            "value": "",
            "linkStart": [
                ""
            ],
            "linkStop": [
                ""
            ],
            "responses": [
                ""
            ]
        }
    ]
}

def translate_name(name):
    return name.replace(':', '_')

class StepParser:
    def __init__(self, step_loaded, dialogs_loaded):
        if (type(step_loaded) != dict):
            raise TypeError("step_loaded should be a dict")
        if (type(dialogs_loaded) != dict):
            raise TypeError("dialogs_loaded should be a dict")
        self.steps = step_loaded
        self.dialogs = dialogs_loaded
        self.conditions_loaded = 0
        self.response_loaded = 0
        self.start_link = 0
        self.stop_link = 0
        self.step_list = self.processAllSteps()


    def dialogResponses(self, dialogId):
        result = []
        dialog = self.dialogs[dialogId]

        for message in dialog["messages"]:
            result += message["responses"]

        result += dialog["endResponses"]
        return result

    def textMenuResponses(self, textMenu):
        result = []

        for choice in textMenu["choices"]:
            result += choice["responses"]

        return result

    def responseListParser(self, responseList):
        result = []
        for response in responseList:
            temp = {"id": response["@type"], "value": "", "linkStart": [], "linkStop": [], "responses": []}
            if (temp["id"] == "StartStep"):
                temp["linkStart"].append(response["stepId"])
                self.start_link += 1
            elif (temp["id"] == "EndStep"):
                temp["linkStop"].append(response["stepId"])
                self.stop_link += 1
            elif (temp["id"] == "CreateDialog"):
                temp["value"] = response["dialogId"]
                try:
                    temp["responses"] += self.responseListParser(self.dialogResponses(response["dialogId"]))
                except KeyError:
                    print("No responses field found on Dialog " + response["dialogId"])
            elif (temp["id"] == "PlayTextMenu"):
                try:
                    temp["responses"] += self.responseListParser(self.textMenuResponses(response))
                except:
                    print("Missing field on TextMenu")

            self.response_loaded += 1
            result.append(temp)
        return result


    def stepParser(self, step_dict_key, step_dict_value):
        result = {"id" : step_dict_key, "conditions" : [], "responses": []}

        for condition in step_dict_value["conditionList"]:
            result["conditions"].append(condition["@type"])
            self.conditions_loaded += 1

        result["responses"] += self.responseListParser(step_dict_value["rewardList"])
        return result

    def processAllSteps(self):
        result = []
        for stepKey, stepValue in self.steps.items():
            result.append(self.stepParser(stepKey, stepValue))

        return result
