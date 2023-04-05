import argparse
import sys

from GraphMaker import *
from JsonVisualiser import JsonLoader
from StepParser import StepParser

QUEST_FOLDER_PATH = None
DIALOG_FOLDER_PATH = None
OUTPUT_NAME = "./output/idralwelGraph"  # CAN NOT BE graph


def args_parsing():
    global QUEST_FOLDER_PATH, DIALOG_FOLDER_PATH, OUTPUT_NAME
    parser = argparse.ArgumentParser(
        description="Idralwel Json Visualiser let you create and store dot graph out of special JSON formatted Adventure based off the Idralwel Project")
    parser.add_argument('-f', '--folder', action='store',
                        help="The Adventure folder to search from, needs to have a quest folder and Dialogs folder in it")
    parser.add_argument('-o', '--output', action='store',
                        help="The output file name to create (do not include extension)")
    parser.add_argument('-v', '--vertical', action='store_true',
                        help="The output graph will be vertical, default horizontal")
    parser.add_argument('--pdf', action='store_true', help="Output a pdf file")
    parser.add_argument('--dot', action='store_true', help="Output a dot file")
    parser.add_argument('--png', action='store_true', help="Output a png file")

    result = parser.parse_args()
    print("L. Argument Parsing")
    if result.folder == None:
        print("|\tError, folder must be specified using option -f or --file\n|\tOption -h or --help for help\n'")
        sys.exit()
    if result.output == None:
        print("|\tWarning, output file not defined, created ./output/idralwelGraph by default\n|\tCan be specified using option -o or --output\n|\tOption -h or --help for help\n'")
    elif result.output == "graph":
        print(f"|\t{result.output} is an invalid name, using default name ./output/idralwelGraph\n'")
    print("|\tArgs : ", result.__dict__.__str__()[1:-1])
    QUEST_FOLDER_PATH = result.folder+"/quest/"
    DIALOG_FOLDER_PATH = result.folder+"/Dialogs/"
    OUTPUT_NAME = result.output
    return result


if __name__ == '__main__':
    print("[Idralwel Json Visualiser]")

    args = args_parsing()
    print("L. Loading Files")
    jsonLoader = JsonLoader(QUEST_FOLDER_PATH, DIALOG_FOLDER_PATH)
    dialogs = jsonLoader.dialogs_list
    quests = jsonLoader.json_list
    print(f"|\tLoaded {len(quests)} quests from {QUEST_FOLDER_PATH}")
    print(f"|\tLoaded {len(dialogs)} dialogs from {DIALOG_FOLDER_PATH}")
    for json in quests.keys():
        print(f"L. Loading {json}...")
        stepParser = StepParser(jsonLoader.json_list[json]["steps"], jsonLoader.dialogs_list)
        print(f"|\tLoaded {len(stepParser.steps)} steps")
        print(f"|\tLoaded {stepParser.conditions_loaded} conditions")
        print(f"|\tLoaded {stepParser.response_loaded} responses")
        print(f"|\tLoaded {stepParser.start_link} start link")
        print(f"|\tLoaded {stepParser.stop_link} stop link")
        print("'\t Done !")

        print(f"+\tStarting graph generation for {json}...")
        print("|\tThat can take a few seconds !")
        create_step_graph(stepParser, OUTPUT_NAME, pdf=args.pdf, png=args.png, dot=args.dot,
                          horizontal=not args.vertical)
        print("'\t Done !")
