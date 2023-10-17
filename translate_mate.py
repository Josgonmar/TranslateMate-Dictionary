from colorama import Fore, Style, init
import json
import signal
import sys
import os

init(autoreset=True)

class MainProgram:

    def __init__(self, file_path):
        self.__folder_path = file_path
        self.__data_lists = {"noun": [], "verb": [], "adjective": [], "adverb": []}
        self.__has_changes = False

        def signalHandler(signum, frame):
            self.__saveAndExit()

        signal.signal(signal.SIGINT, signalHandler)
        signal.signal(signal.SIGTERM, signalHandler)

    def __saveAndExit(self):
        if self.__has_changes:
            for file_type, data_list in self.__data_lists.items():
                file_path = os.path.join(self.__folder_path, f'{file_type}.json')
                try:
                    with open(file_path, "w") as file:
                        json.dump(data_list, file, indent=4)
                    print(Fore.GREEN + f"Data saved successfully for {file_type}.json.")
                except (FileNotFoundError, PermissionError, json.JSONEncodeError) as e:
                    print(Fore.RED + f"Error while saving data for {file_type}.json: {e}")
            print(Fore.GREEN + "Goodbye!")
        else:
            print(Fore.GREEN + "Goodbye!")
        sys.exit(0)

    def __loadData(self):
        try:
            for file_type, data_list in self.__data_lists.items():
                file_path = os.path.join(self.__folder_path, f'{file_type}.json')
                try:
                    with open(file_path, "r") as file:
                        self.__data_lists[file_type] = json.load(file)
                        print(Fore.LIGHTGREEN_EX + f"[Successfully loaded a total of '{len(self.__data_lists[file_type])}' "
                               + f"{file_type}s from local]")
                except FileNotFoundError as e:
                    print(Fore.YELLOW + f"[JSON file for '{file_type}' not found. Creating an empty dictionary locally]")
                    with open(file_path, "w") as file:
                        json.dump(data_list, file, indent=4)
                except json.JSONDecodeError as e:
                    print(Fore.RED + f"Error while loading data for {file_type}.json: {e}")
        except Exception as e:
            print(Fore.LIGHTRED_EX + f"[An error occurred while loading data: {str(e)}]")

    def __addWord(self):
        w_type = input("Enter your choice: ")

        if w_type == '1':
            print(Fore.LIGHTGREEN_EX + "Let's add a new noun to the list!")
            self.__addNewNoun()
        elif w_type == '2':
            print(Fore.LIGHTGREEN_EX + "Let's add a new verb to the list!")
            self.__addNewVerb()
        elif w_type == '3':
            print(Fore.LIGHTGREEN_EX + "Let's add a new adjective to the list!")
            self.__addNewAdjective()
        elif w_type == '4':
            print(Fore.LIGHTGREEN_EX + "Let's add a new adverb to the list!")
            self.__addNewAdverb()
        elif w_type == '5':
            return
        else:
            print(Fore.RED + "Invalid choice. Please select a valid option.")
            self.__addWord()

    def __addNewNoun(self):
        try:
            english = {"EN": input("EN: ")}
            german = {"DE": input("DE: ")}
            gender = {"GENDER": input("GENDER (DE): ")}
            plural = {"PLURAL": input("PLURAL (DE): ")}

            new_word = [english, german, gender, plural]

            print(f"So, you entered: '{new_word}'")

            if self.__askPromptCorrect(self.__addNewNoun):
                self.__data_lists["noun"].append(new_word)
                self.__has_changes = True
                print(Fore.LIGHTGREEN_EX + "New entry added!\n")
        except Exception as e:
            print(Fore.RED + f"Error while adding a new noun: {e}")

    def __addNewVerb(self):
        try:
            english = {"EN": input("EN: ")}
            german = {"DE": input("DE: ")}
            partizip = {"PARTIZIP": input("PARTIZIP: ")}

            new_word = [english, german, partizip]

            print(f"So, you entered: '{new_word}'")

            if (self.__askPromptCorrect(self.__addNewVerb)):
                self.__data_lists["verb"].append(new_word)
                self.__has_changes = True
                print(Fore.LIGHTGREEN_EX + "New entry added!\n")
        except Exception as e:
            print(Fore.RED + f"Error while adding a new verb: {e}")

    def __addNewAdjective(self):
        try:
            english = {"EN": input("EN: ")}
            german_m = {"DE_M": input("DE_M: ")}
            german_f = {"DE_F": input("DE_F: ")}
            german_n = {"DEF_N": input("DE_N: ")}

            new_word = [english, german_m, german_f, german_n]

            print(f"So, you entered: '{new_word}'")

            if (self.__askPromptCorrect(self.__addNewAdjective)):
                self.__data_lists["adjective"].append(new_word)
                self.__has_changes = True
                print(Fore.LIGHTGREEN_EX + "New entry added!\n")
        except Exception as e:
            print(Fore.RED + f"Error while adding a new adjective: {e}")

    def __addNewAdverb(self):
        try:
            english = {"EN": input("EN: ")}
            german = {"DE": input("DE: ")}

            new_word = [english, german]

            print(f"So, you entered: '{new_word}'")

            if (self.__askPromptCorrect(self.__addNewAdverb)):
                self.__data_lists["adverb"].append(new_word)
                self.__has_changes = True
                print(Fore.LIGHTGREEN_EX + "New entry added!\n")
        except Exception as e:
            print(Fore.RED + f"Error while adding a new adverb: {e}")

    def __askPromptCorrect(self, function):
        answer = input("Is it correct? (YES/no): ")
        if answer.strip().upper() == "YES" or answer.strip().lower() == "y" or not answer:
            return True
        elif answer.strip().upper() == "NO" or answer.strip().lower() == "n":
            function()
            return False
        else:
            return self.__askPromptCorrect()
        
    def __AskPromptGoAhead(self):
        answer = input("(YES/no): ")
        if answer.strip().upper() == "YES" or answer.strip().lower() == "y" or not answer:
            return True
        elif answer.strip().upper() == "NO" or answer.strip().lower() == "n":
            return False
        else:
            return self.__AskPromptGoAhead()
        
    def __findWord(self):
        word_to_look_for = input("Enter word: ")
        somethingFound = False

        for file_type, data_list in self.__data_lists.items():
            for entry in data_list:
                for dict in entry:
                    for _, value in dict.items():
                        if (value.strip().lower() == word_to_look_for.strip().lower()):
                            somethingFound = True
                            print(Fore.LIGHTMAGENTA_EX + f"Found a '{file_type}': '{entry}'")
        
        if (not somethingFound):
            print(Fore.LIGHTRED_EX + "Word not found. Would you like to add it?")
            if (self.__AskPromptGoAhead()):
                self.__displayWordMenu()
                self.__addWord()

    def __removeWord(self):
        word_to_look_for = input("Enter word: ")

        for file_type, data_list in self.__data_lists.items():
            entries_to_remove = []

            for entry in data_list:
                for dict in entry:
                    for _, value in dict.items():
                        if (value.strip().lower() == word_to_look_for.strip().lower()):
                            print(Fore.LIGHTMAGENTA_EX + f"Found a '{file_type}': '{entry}'")
                            print(Fore.LIGHTGREEN_EX + "Would you like to remove it?")
                            if (self.__AskPromptGoAhead()):
                                entries_to_remove.append(entry)

            for entry in entries_to_remove:
                data_list.remove(entry)
                self.__has_changes = True
                print(Fore.RED + "Word removed.")
        
    def __displayWordMenu(self):
        print(Fore.GREEN + "Ok, which type of word is it?:")
        print(Fore.BLUE + "1. Noun.")
        print(Fore.BLUE + "2. Verb.")
        print(Fore.BLUE + "3. Adjective.")
        print(Fore.BLUE + "4. Adverb.")
        print(Fore.RED + "5. Go back")

    def __displayMainMenu(self):
        print(Fore.GREEN + "Please, select one of the available options down below:")
        print(Fore.BLUE + "1. Add a new word.")
        print(Fore.BLUE + "2. Look for an existing word.")
        print(Fore.BLUE + "3. Remove an existing word.")
        print(Fore.RED + "4. Quit")

    def run(self):

        self.__loadData()

        print("\n" + Fore.GREEN + "Welcome to " + Fore.CYAN + "TranslateMate" + Fore.GREEN + ", an interactive EN-DE dictionary!")

        while True:
            self.__displayMainMenu()

            print(Style.RESET_ALL)
            choice = input("Enter your choice: ")

            if choice == '1':
                print(Fore.LIGHTGREEN_EX + "Let's add a new word to the list!")
                self.__displayWordMenu()
                self.__addWord()
            elif choice == '2':
                print(Fore.LIGHTGREEN_EX + "Let's find that word for you!")
                self.__findWord()
            elif choice == '3':
                print(Fore.LIGHTGREEN_EX + "Let's get rid of that word for good!")
                self.__removeWord()
            elif choice == '4' or choice.strip().lower() == 'q':
                self.__saveAndExit()
                break
            else:
                print(Fore.RED + "Invalid choice. Please select a valid option.")



if __name__ == "__main__":
    main = MainProgram("./data")
    main.run()