#   Author: Ryan Coplien
#   Project: Diceware Test Project
#   Description: Application that uses different word lists and python to automatically generate passphrases via
#                Diceware to make memorable, secure passwords.

# TODO: Use pip freeze and requirements file for github venv
# TODO: Maybe make this into a GUI application?
import secrets


def main():
    print("Welcome to Diceware password creation!")
    # TODO: Create Config settings to select different word lists from selection
    selection = input("Choose from the following actions:\n"
                      "1) Generate Diceware Passphrase\n"
                      "2) Configure Word Count\n"
                      "3) Select Word List\n")
    match selection:
        case 1: create_passphrase()
        case 2: config_word_count()
        case 3: config_word_list()
        case _: main()
    # TODO: Utilize configuration file settings in order to continue application


def create_passphrase():
    print(f"Rolling for {word_count} words using the {word_list}")
    number_list = generate_numbers(word_count)
    print(number_list)


# TODO: Change function name, split functions if needed
def config_word_count():
    try:
        # Personal recommendation is no more than 7 words due to reaching limits of human memory,
        # Personal recommendation is 5 or more words due to brute forcing times
        word_count = int(input("How many words would you like to do use? You can select 1 - 8 words.\n"))
        if word_count > 0 or word_count <= 8:
            print(f"Set word count to {word_count}.")
            update_config("Count", word_count)
            # TODO: Set config word count here
        else:
            print("Please between 1 and 8 words!")
    except ValueError:
        print("Please enter a number!")
    config_word_count()


def config_word_list():
    try:
        selection = input("What word list would you like to use? (1 - 3)\n"
                          "1) EFF Long List (Recommended)\n"
                          "2) EFF Short List\n"
                          "3) Original Diceware List\n")
        if selection in [1, 2, 3]:
            # TODO: Look into ENUM for python
            print(f"Set word list to {selection}")
            update_config("List", selection)
        else:
            print("Please select a number 1 - 3")
    except ValueError:
        print("Please enter a number 1 - 3.")
    config_word_list()


def update_config(config_setting, config_option):
    print("DO SOMETHING")
    # TODO: Update config settings right here


def read_config():
    # TODO: Read from config file here
    return 0


def generate_numbers(word_count):
    count = 0
    full_dice_roll = ""
    dice_rolls = []
    # TODO: Add variable number based on wordlist here, CONSIDER SWITCHING TO FOR LOOP?
    # TODO: Potentially use arrays for word lists to have dice count?
    while count < (word_count * 4): # TODO: Make this number a variable
        # Concatenate numbers, keep in string format
        full_dice_roll = f"{full_dice_roll}{dice_roll()}"
        count += 1
        if count % 4 == 0:
            dice_rolls.append(full_dice_roll)
            full_dice_roll = ""
    return dice_rolls


def dice_roll():
    # Using secrete module to generate random dice rolls, as it is cryptographically secure.
    return secrets.choice("123456")  # Use string, as conversion to int is not needed later


def parse_words():
    # TODO: Make file variable, might be good to use array for wordlist
    with open("..\\lists\\EFF Short List.txt") as f:
        line = f.readline()
        while line:
            line = f.readline()
            # Number associated with word: print(line[0:4])
            # Actual word: print(line[5:])


if __name__ == "__main__":
    main()
