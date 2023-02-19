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
SHEET = GSPREAD_CLIENT.open('VetSeed')

profile = SHEET.worksheet('profile')

data = profile.get_all_values()

print(data)


def introduction():
    """
    define goal of program
    Create function for introduction of topic
    """
    while True:
        print("Welcome to VetSeed, program to authomate data for all vets.")
        print("Answer the next questions to calcolate dog's per day calories")
        print("Please insert first name of dog")
        print("Example: Bob\n")

        data_name = input("Name of dog:\n")

        saved_name = data_name

        if validate_info(saved_name):
            print(f"Name of dog provided is {saved_name}")
            break

    return saved_name



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

    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")
        return False

    return True


introduction()