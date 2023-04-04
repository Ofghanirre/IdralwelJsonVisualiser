from GraphMaker import *
from JsonVisualiser import JsonLoader
from StepParser import StepParser

QUEST_FOLDER_PATH = "./json/IdralwelMain/quest/"
DIALOG_FOLDER_PATH = "./json/IdralwelMain/Dialogs/"
OUTPUT_NAME = "idralwelGraph" # CAN NOT BE graph


if __name__ == '__main__':
    print("Idralwel JSON Visualiser")
    jsonLoader = JsonLoader(QUEST_FOLDER_PATH, DIALOG_FOLDER_PATH)
    dialogs = jsonLoader.dialogs_list
    quests = jsonLoader.json_list
    print(f"Loaded {len(quests)} quests from {QUEST_FOLDER_PATH}")
    print(f"Loaded {len(dialogs)} dialogs from {DIALOG_FOLDER_PATH}")
    for json in quests.keys():
        print(f"Loading {json}...")
        stepParser = StepParser(jsonLoader.json_list[json]["steps"], jsonLoader.dialogs_list)
        print(f"|\tLoaded {len(stepParser.steps)} steps")
        print(f"|\tLoaded {stepParser.conditions_loaded} conditions")
        print(f"|\tLoaded {stepParser.response_loaded} responses")
        print(f"|\tLoaded {stepParser.start_link} start link")
        print(f"|\tLoaded {stepParser.stop_link} stop link")
        print("'\t Done !")


        print(f"Starting graph generation for {json}...")
        print("That can take a few seconds !")
        create_step_graph(stepParser, OUTPUT_NAME)
        print("'\t Done !")
