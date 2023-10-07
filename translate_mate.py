from colorama import Fore, Style, init
import json
import signal
import sys

init(autoreset=True)

class MainProgram:

    def __init__(self, file_path):
        self.file_path = file_path
        self.__data = []


    def __save_and_exit(self):
        with open(self.file_path, "w") as file:
            json.dump(self.__data, file, indent=4)
        print(Fore.GREEN + "Data saved successfully. Goodbye!")
        sys.exit(0)

    def __load_data(self):
        try:
            with open(self.file_path, "r") as file:
                self.__data = json.load(file)
            print(Fore.GREEN + "Data loaded successfully.")
        except FileNotFoundError:
            print(Fore.YELLOW + "JSON file not found. Creating an empty dictionary.")
            with open(self.file_path, "w") as file:
                json.dump(self.__data, file, indent=4)

    def __add_word(self):
            
            def ask_prompt():
                answer = input("Is it correct? (YES/no): ")
                if answer.strip().upper() == "YES" or not answer:
                    return True
                elif answer.strip().upper() == "NO":
                    self.__add_word()
                    return False
                else:
                    return ask_prompt()

            english = {"EN": input("EN: ")}
            german = {"DE": input("DE: ")}

            new_word = [english, german]

            print(f"About to add '{english}' and its German translation '{german}' to the dictionary.")

            if (ask_prompt()):
                self.__data.append(new_word)

    def __display_menu(self):
        print(Fore.GREEN + "Please, select one of the available options down below:")
        print(Fore.BLUE + "1. Add a new word.")
        print(Fore.BLUE + "2. Look for an existing word.")
        print(Fore.BLUE + "3. Remove an existing word.")
        print(Fore.RED + "4. Quit")

    def run(self):

        def signal_handler(signum, frame):
            self.__save_and_exit()

        signal.signal(signal.SIGINT, signal_handler)

        self.__load_data()

        print(Fore.GREEN + "Welcome to TranslateMate, an interactive EN-DE dictionary!")

        while True:
            self.__display_menu()

            print(Style.RESET_ALL)
            choice = input("Enter your choice: ")

            if choice == '1':
                self.__add_word()

            elif choice == '2':
                print("You selected Option 2. It does nothing just yet!")

            elif choice == '3':
                print("You selected Option 3. It does nothig just yet!")

            elif choice == '4':
                self.__save_and_exit()
                break
            else:
                print(Fore.RED + "Invalid choice. Please select a valid option.")



if __name__ == "__main__":
    main = MainProgram("./data/dictionary.json")
    main.run()