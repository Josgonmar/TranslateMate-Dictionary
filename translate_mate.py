from colorama import Fore, Style, init
import json
import signal
import sys

init(autoreset=True)

class MainProgram:

    def __init__(self, file_path):
        self.__folder_path = file_path
        self.__data_lists = {"nomen": [], "verb": [], "adjektiv": [], "adverb": []}
        self.__hasChanges = False

        def signal_handler(signum, frame):
            self.__save_and_exit()

        signal.signal(signal.SIGINT, signal_handler)

    def __save_and_exit(self):
        if (self.__hasChanges):
            for file_type, data_list in self.__data_lists.items():
                file_path = self.__folder_path + '/' + file_type + '.json'
                with open(file_path, "w") as file:
                    json.dump(data_list, file, indent=4)

            print(Fore.GREEN + "Data saved successfully. Goodbye!")
        else:
            print(Fore.GREEN + "Goodbye!")
        sys.exit(0)

    def __load_data(self):
        try:
            for file_type, data_list in self.__data_lists.items():
                file_path = self.__folder_path + '/' + file_type + '.json'
                with open(file_path, "r") as file:
                    data_list = json.load(file)
                    print(Fore.LIGHTGREEN_EX + f"[Successfully loaded a total of: '{len(data_list)}' " + file_type + " from local]")

        except FileNotFoundError:
            print(Fore.YELLOW + "[JSON file not found. Creating an empty dictionary locally]")
            for file_type, data_list in self.__data_lists.items():
                file_path = self.__folder_path + '/' + file_type + '.json'
                with open(file_path, "w") as file:
                    json.dump(data_list, file, indent=4)

    def __add_word(self):
        w_type = input("Enter your choice: ")

        if w_type == '1':
            print(Fore.LIGHTGREEN_EX + "Let's add a new noun to the list!")
            self.__add_new_noun()
        elif w_type == '2':
            print(Fore.LIGHTGREEN_EX + "Let's add a new verb to the list!")
            self.__add_new_verb()
        elif w_type == '3':
            print(Fore.LIGHTGREEN_EX + "Let's add a new adjective to the list!")
            self.__add_new_adjective()
        elif w_type == '4':
            print(Fore.LIGHTGREEN_EX + "Let's add a new adverb to the list!")
            self.__add_new_adverb()
        elif w_type == '5':
            return
        else:
            print(Fore.RED + "Invalid choice. Please select a valid option.")
            self.__add_word()

    def __add_new_noun(self):
        english = {"EN": input("EN: ")}
        german = {"DE": input("DE: ")}
        gender = {"GENDER": input("GENDER (DE): ")}
        plural = {"PLURAL": input("PLURAL (DE): ")}

        new_word = [english, german, gender, plural]

        print(f"So, you entered: '{new_word}'")

        if (self.__ask_prompt_correct(self.__add_new_noun)):
            self.__data_lists["nomen"].append(new_word)
            self.__hasChanges = True
            print(Fore.LIGHTGREEN_EX + "New entry added!\n")

    def __add_new_verb(self):
        english = {"EN": input("EN: ")}
        german = {"DE": input("DE: ")}
        partizip = {"PARTIZIP": input("PARTIZIP: ")}

        new_word = [english, german, partizip]

        print(f"So, you entered: '{new_word}'")

        if (self.__ask_prompt_correct(self.__add_new_verb)):
            self.__data_lists["verb"].append(new_word)
            self.__hasChanges = True
            print(Fore.LIGHTGREEN_EX + "New entry added!\n")

    def __add_new_adjective(self):
        english = {"EN": input("EN: ")}
        german_m = {"DE_M": input("DE_M: ")}
        german_f = {"DE_F": input("DE_F: ")}
        german_n = {"DEF_N": input("DE_N: ")}

        new_word = [english, german_m, german_f, german_n]

        print(f"So, you entered: '{new_word}'")

        if (self.__ask_prompt_correct(self.__add_new_adjective)):
            self.__data_lists["adjektiv"].append(new_word)
            self.__hasChanges = True
            print(Fore.LIGHTGREEN_EX + "New entry added!\n")

    def __add_new_adverb(self):
        english = {"EN": input("EN: ")}
        german = {"DE": input("DE: ")}

        new_word = [english, german]

        print(f"So, you entered: '{new_word}'")

        if (self.__ask_prompt_correct(self.__add_new_adverb)):
            self.__data_lists["adverb"].append(new_word)
            self.__hasChanges = True
            print(Fore.LIGHTGREEN_EX + "New entry added!\n")

    def __ask_prompt_correct(self, function):
        answer = input("Is it correct? (YES/no): ")
        if answer.strip().upper() == "YES" or answer.strip().lower() == "y" or not answer:
            return True
        elif answer.strip().upper() == "NO" or answer.strip().lower() == "n":
            function()
            return False
        else:
            return self.__ask_prompt_correct()
        
    def __display_word_menu(self):
        print(Fore.GREEN + "Ok, which type of word is it?:")
        print(Fore.BLUE + "1. Noun.")
        print(Fore.BLUE + "2. Verb.")
        print(Fore.BLUE + "3. Adjective.")
        print(Fore.BLUE + "4. Adverb.")
        print(Fore.RED + "5. Go back")

    def __display_main_menu(self):
        print(Fore.GREEN + "Please, select one of the available options down below:")
        print(Fore.BLUE + "1. Add a new word.")
        print(Fore.BLUE + "2. Look for an existing word.")
        print(Fore.BLUE + "3. Remove an existing word.")
        print(Fore.RED + "4. Quit")

    def run(self):

        self.__load_data()

        print("\n" + Fore.GREEN + "Welcome to " + Fore.CYAN + "TranslateMate" + Fore.GREEN + ", an interactive EN-DE dictionary!")

        while True:
            self.__display_main_menu()

            print(Style.RESET_ALL)
            choice = input("Enter your choice: ")

            if choice == '1':
                print(Fore.LIGHTGREEN_EX + "Let's add a new word to the list!")
                self.__display_word_menu()
                self.__add_word()
            elif choice == '2':
                print("You selected Option 2, but it does nothing just yet!")
            elif choice == '3':
                print("You selected Option 3, but it does nothig just yet!")
            elif choice == '4' or choice.strip().lower() == 'q':
                self.__save_and_exit()
                break
            else:
                print(Fore.RED + "Invalid choice. Please select a valid option.")



if __name__ == "__main__":
    main = MainProgram("./data")
    main.run()