#   Author: Ryan Coplien
#   Project: Diceware Test Project
#   Description: Application that uses different word lists and python to automatically generate passphrases via
#                Diceware to make memorable, secure passwords.


# TODO         ROADMAP:
# TODO              Full functionality (Testing, deploying to github, readme, etc)
# TODO              Config file to save settings
# TODO              Batch mode for servers
# TODO              New languages
# TODO              More Lists
# TODO              *POTENTIALLY* GUI for application via html and javascript?

# TODO: Use pip freeze and requirements file for github venv
# TODO: Maybe make this into a GUI application?
import secrets

# Word list structure [list number, list file name, dice rolls per word]
word_lists = (  # TODO: Consider making this an object?
    [1, "EFF Large List", 5],
    [2, "EFF Short List", 4],
    [3, "Original Diceware List", 5]
)

# Invalid defaults to set variables
word_count = -1
word_list = -1


# Debug function for testing
def debug():
    print("Set to debug mode")


def main():
    print("Welcome to Diceware password creation!")
    init()
    choose_actions()


def prompt_repeat():
    selection = input("Would you like to generate another passphrase? (Y or N)\n")
    if selection == "Y":  # TODO: Set this to check for correct string (lowercase and uppercase)
        create_passphrase()
    else:
        exit()


def choose_actions():
    selection = int(input("Choose from the following actions:\n"
                          "1) Generate Diceware Passphrase\n"
                          "2) Configure Word Count\n"
                          "3) Select Word List\n"
                          "4) Exit\n"))
    match selection:
        case 1:
            create_passphrase()
        case 2:
            config_word_count()
        case 3:
            config_word_list()
        case 4:
            exit()
        case _:
            choose_actions()
    choose_actions()


# Function to initialize configuration settings
def init():
    global word_count
    global word_list
    # word_count = read_config("Count")
    # word_list = read_config("List")
    if word_count == -1:
        word_count = 5
    if word_list == -1:
        word_list = 0
    # TODO: Pull from config file here then if no config file, create it using defaults


def create_passphrase():
    print(f"Rolling for {word_count} words using {word_lists[word_list][1]}")
    number_list = generate_numbers()
    print(number_list)
    # parse_words(number_list)
    prompt_repeat()


def config_word_count():
    try:
        # Personal recommendation is no more than 7 words due to reaching limits of human memory,
        # Personal recommendation is 5 or more words due to brute forcing times
        selection = int(input("How many words would you like to do use? You can select 1 - 8 words.\n"))
        if selection > 0 or selection <= 8:
            update_config("Count", selection)
        else:
            print("Please between 1 and 8 words!")
            config_word_count()
    except ValueError:
        print("Please enter a number!")
        config_word_count()


def config_word_list():
    try:
        selection = input("What word list would you like to use? (1 - 3)\n"
                          "1) EFF Large List (Recommended)\n"
                          "2) EFF Short List\n"
                          "3) Original Diceware List\n")
        if selection in [1, 2, 3]:
            update_config("List", selection)
        else:
            print("Please select a number 1 - 3")
            config_word_list
    except ValueError:
        print("Please enter a number 1 - 3.")
        config_word_list()


def update_config(config_setting, config_option):
    global word_count
    global word_list
    if config_setting == "Count":
        word_count = config_option
        # TODO: Update config file word count settings here
        print(f"Set word count to {config_option}")
    elif config_setting == "List":
        word_list = config_option
        # TODO: Update config file word list settings here
        print(f"Set word list to {config_option}")
    else:
        print("There was an error updating config settings - Invalid config setting")


def read_config():
    # TODO: Read from config file here
    return -1


def edit_config():
    # TODO: Edit config file function here
    print("Update config file directly here")


def generate_numbers():
    count = 0
    current_number = ""
    number_list = []
    num_length = word_lists[word_list][2]
    while count < (word_count * num_length):
        # Concatenate numbers, keep in string format
        current_number = f"{current_number}{dice_roll()}"
        count += 1
        if count % num_length == 0:
            number_list.append(current_number)
            current_number = ""
    return number_list


def dice_roll():
    # Using secrete module to generate random dice rolls, as it is cryptographically secure.
    return secrets.choice("123456")  # Use string, as conversion to int is not needed later


def parse_words():
    with open(f"..\\lists\\{word_lists[word_list][1]}.txt") as f:
        line = f.readline()
        while line:
            line = f.readline()
            # Number associated with word: print(line[0:4])
            # Actual word: print(line[5:])


if __name__ == "__main__":
    main()
    # debug()
