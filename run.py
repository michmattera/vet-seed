import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]


CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('VetSeed').sheet1

print(SHEET.cell(1,1).value)


def introduction():
    """
    define goal of program
    """
    #profile = SHEET.worksheet('profile')
    #data = profile.get_all_values()
    # print(data)
    while True:
        print("Please insert first name of dog")
        print("Example: Bob\n")

        data_name = input("Name of dog:\n")
        saved_name = data_name

        if validate_info(saved_name):
            print(f"Thank you")
            print(f"Name of dog provided is {saved_name}\n")
            break

    return saved_name

def just_info():
    """
    give user choice
    Create function for introduction of topic
    choose between get just general information or go and calcolate dog's per day calories\n
    """
    print("Welcome to VetSeed, program to authomate data for all vets.")
    while True:
        print("Please choose what would you like to know")
        print("Do you want to?\n")
        choice = input("A) Get general info.\n B) Calcolate calories. [A/B]?:")
        if choice == "A" or "a":
            print("General info loading...")
            general_info()
        elif choice == "B" or "b":
            print("Please answer the following questions.")
        elif choice == "Q":
            print("Done!")
        break

def general_info():
    """
    List general info and give another choice to user
    Let user choose if he wants to calcolate calories
    Or is done and do not need anything else
    """
    print("Example instrucion here...")
    choice_two = input("A) Calcolate calories .\n B) End program. [A/B]?:")
    if choice_two == "A" or "a":
        print("Please answer following questions:")
        introduction()
    elif choice_two == "B" or "b":
        print("Thank you come back soon.")



def dogs_weight():
    """
    Ask user to insert weight of dog
    Check that right input was provided
    """
    print("Please provide weight of dog")
    print("Please provide exact weight from 0 to 100 kg")
    while True:
        data_weight = input("Weight of dog:")
        saved_weight = data_weight

        if validate_weight(saved_weight):
            print(f"Weight of dog provided is {saved_weight}\n")
            break
    return saved_weight


def validate_weight(saved_weight):
    """
    Validate weight
    check if value was between 0 and 100
    check if values was not a letter
    give error if invalid value or empty
    """
    try:
        if not saved_weight:
            raise ValueError(
                f"Field cannot be left blank"
            )
            return False

        [int(value) for value in saved_weight]
        if int(saved_weight) <= 0 or int(saved_weight) > 100:
            raise ValueError(
                f"Please insert value between 0 and 100"
            )
            return False

    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")
        return False

    return True


def validate_info(values):
    """
    Validate info
    gave error if more that 10 letters
    gave error if number or if more than one world was given
    """
    try:
        if len(values) > 10:
            raise ValueError(
                f"Max lenght of name is 10 letters you gave {len(values)}"
            )
            return False

        if not values:
            raise ValueError(
                f"Field cannot be left blank"
            )
            return False

    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")
        return False

    return True

def dogs_bcs():
    """
    Ask user to insert bcs of dog
    Check that right input was provided
    Useing validate_bcs to validate info from user
    """
    print("Please provide bcs of dog")
    print("Bcs should be a value between 1 and 9")
    while True:
        data_bcs = input("Bcs of dog:")
        saved_bcs = data_bcs

        if validate_bcs(saved_bcs):
            print(f"Bcs of dog provided is {saved_bcs}")
            break
    return saved_bcs


def validate_bcs(saved_bcs):
    """
    Function to get body score condition of dog
    Correct value should be from 1 to 9
    Give error to user for invalid value
    """
    try:
        if not saved_bcs:
            raise ValueError(
                f"Field cannot be left blank"
            )
            return False

        [int(value) for value in saved_bcs]
        if int(saved_bcs) <= 0 or int(saved_bcs) >= 10:
            raise ValueError(
                f"Please insert value between 1 and 9"
            )
            return False

    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")
        return False

    return True

def calcolate_target_weight(new_bcs, new_weight):
    """
    Get bcs and weight from dogs_weight and dogs_bcs
    Use correct formula to calcolate correct weight
    Let the user know if dog is under-over or correct weight
    """
    target_weight = new_weight * [100 % (100 + (new_bcs - 5) * 10)]
    print(target_weight)


def main():
    just_info()
    general_info()
    introduction()
    dogs_weight()
    dogs_bcs()
    #new_weight = dogs_weight()
    #new_bcs = dogs_bcs()
    #calcolate_target_weight(new_bcs, new_weight)
    print(saved_weight)
    print(saved_bcs)


main()
