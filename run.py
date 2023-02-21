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
    Create function for introduction of topic
    """
    #profile = SHEET.worksheet('profile')
    #data = profile.get_all_values()
    # print(data)
    print("Welcome to VetSeed, program to authomate data for all vets.")
    print("Answer the next questions to calcolate dog's per day calories\n")
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
            print(f"Weight of dog provided is {saved_weight}")
            break
    return saved_weight


def validate_weight(saved_weight):
    """
    Validate weight
    check if value was between 0 and 100
    check if values was not a letter
    give error if invalid error
    """
    try:
        if not saved_weight:
            raise ValueError(
                f"Field cannot be left blank"
            )
            return False

        [int(value) for value in saved_weight]
        if int(saved_weight) < 0 or int(saved_weight) > 100:
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


def main():
    introduction()
    dogs_weight()


main()
