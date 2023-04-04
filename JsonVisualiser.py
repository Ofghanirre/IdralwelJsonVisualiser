import json
import os


class JsonLoader:
    def __init__(self, quest_folder_path, dialog_folder_path):
        self.folder_path = quest_folder_path
        self.file_list = self.scan_folder(quest_folder_path)
        self.json_list = self.load_json()
        self.dialogs_list = self.load_dialogs(dialog_folder_path)

    def scan_folder(self, folder_path) -> list:
        result = []
        for filename in os.listdir(folder_path):
            file_path = os.path.join(folder_path, filename)
            if os.path.isfile(file_path):
                result.append(file_path)
            elif os.path.isdir(file_path):
                result += self.scan_folder(file_path)
        return result

    def load_json(self) -> dict:
        result = {}
        for file_path in self.file_list:
            try:
                with open(file_path, "r") as file:
                    result[file_path] = json.load(file)
            except json.decoder.JSONDecodeError:
                with open(file_path, "r", encoding='utf-16') as file:
                    result[file_path] = json.load(file)
        return result

    def load_dialogs(self, dialog_folder_path):
        result = {}
        for file_path in self.scan_folder(dialog_folder_path):
            try:
                with open(file_path, "r") as file:
                    jsonValue = json.load(file)
                    result[jsonValue["id"]] = jsonValue
            except json.decoder.JSONDecodeError:
                with open(file_path, "r", encoding='utf-16') as file:
                    jsonValue = json.load(file)
                    result[jsonValue["id"]] = jsonValue
        return result
