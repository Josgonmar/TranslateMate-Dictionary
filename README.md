# TranslateMate-Dictionary

TranslateMate-Dictionary is an interactive English-German dictionary program written in Python. This command-line tool allows users to add, search for, and remove English-German word pairs, providing a simple and convenient way to manage a personal translation dictionary. The program uses JSON files for data storage and offers a menu-driven interface for easy navigation.

## Key Features

- Add new word pairs with English and German translations.
- Search for existing word entries.
- Remove words from the dictionary **[WIP]**.
- Data is saved to a JSON file for persistence.
- User-friendly and colorful console interface.

## Dependencies

The project relies on the following Python libraries:

- [colorama](https://pypi.org/project/colorama/): For adding color to console output.
- [json](https://docs.python.org/3/library/json.html): For handling JSON data.

## Usage

1. Clone this repository.
2. Run `python translate_mate.py` to start the dictionary program.
3. Follow the on-screen menu to interact with the dictionary.

## TODO List

- [x] Implement search functionality.
- [ ] Implement word removal functionality.
- [x] Implement type of word (verb, noun, adj...).
- [x] Implement singular and plural words.

- [ ] Implementation using [numpy](https://numpy.org/doc/stable/) for better performance.
- [ ] Improve input validation and error handling.
- [ ] Enhance user prompts and feedback.
- [ ] Refactor code for better maintainability.
- [ ] Handle duplicate dictionary entries.