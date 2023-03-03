#  import module
import gspread
import bcrypt
from google.oauth2.service_account import Credentials
from art import *
tprint("vet seed","rnd-xlarge")

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
gen_info = SHEET.worksheet('general_info')
data = gen_info.get_all_values()
INFO = []  # stores a list from user input(weight-name-bsc)
WEIGHT = ""  # stores saved_weight
LIFE_STAGE = float()  # depending on life stage different values stored
MER = []  # stores calcolated mer and after append everything to profile

class PasswordDatabase:
    def __init__(self, user, password):
        self.user = user
        self.password = password
        self.data = dict()
    def register(self, user, password):
        if user in self.data:
            print("user already registered")
            return False
        pwd_hash = self.hash_password(password)
        self.data[user] = pwd_hash
        return True
    def login(self, user, password):
        if user not in self.data:
            print("please register")
            return False
        pwd_bytes = password.encode("utf-8")
        return bcrypt.checkpw(pwd_bytes, self.data[user])
    def hash_password(self, password):
        pwd_bytes = password.encode("utf-8")
        salt = bcrypt.gensalt()
        return bcrypt.hashpw(pwd_bytes, salt)

#  https://plainenglish.io/blog/store-passwords-safely-in-python-e38a8c0c8618#log-in-a-user


user = input("Enter user: ")
password = input("Enter password: ")

enter = PasswordDatabase.register(user, password)


def just_info():
    """
    give user choice
    Create function for introduction of topic
    choose between get just general information
    or go and calcolate dog's per day calories
    """
    while True:
        print("Please choose what would you like to know:\n")
        print("Do you want to?")
        print(" 1) Get general info.\n 2) Calcolate calories.")
        choice = input("")
        if choice == "1":
            print("General info loading.")
            display_info()
        elif choice == "2":
            print("Please answer the following questions.")
            main()
        else:
            print('ERROR, Please choose one of the above')
            continue


def dogs_name():
    """
    define goal of program
    ask user to insert name of dog
    validate info and input from user
    append saved value to global variable
    """
    while True:
        print("Please insert first name of dog")
        print("Example: Bob\n")

        data_name = input("Name of dog:\n")
        saved_name = data_name

        if validate_name(saved_name):
            print("Thank you")
            print(f"Name of dog provided is {saved_name}\n")
            INFO.append(saved_name)
            print(INFO)
            break
    return saved_name


def validate_name(saved_name):
    """
    Validate name
    gave error if more that 10 letters
    gave error if number or if more than one world was given
    gave error if empty space
    """
    try:
        if len(saved_name) > 10:
            raise ValueError(
                f"Max lenght of name is 10 letters you gave {len(saved_name)}"
            )

        if not saved_name:
            raise ValueError(
                "Field cannot be left blank"
            )

        if saved_name.isdigit():
            raise ValueError(
                "Numbers are not accepted"
            )      
        if " " in saved_name:
            raise ValueError(
                "no more than one world accepted"
            )

    except ValueError as error:
        print(f"Invalid data: {error}, please try again.\n")
        return False
    return True


def dogs_weight():
    """
    Ask user to insert weight of dog
    Check that right input was provided
    validate info and input from user
    append saved value to global variable
    """
    print("Please provide weight of dog")
    print("Please provide exact weight from 0 to 100 kg")
    while True:
        data_weight = input("Weight of dog:")
        saved_weight = data_weight

        if validate_weight(saved_weight):
            print(f"Weight of dog provided is {saved_weight}\n")
            INFO.append(saved_weight)
            print(INFO)
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
                "Field cannot be left blank"
            )

        if float(saved_weight) <= 0 or float(saved_weight) > 100:
            raise ValueError(
                "Please insert value between 0 and 100"
            )

        if saved_weight.isalpha():
            raise ValueError(
                "Please insert a number"
            )

    except ValueError as error:
        print(f"Invalid data: {error}, please try again.\n")
        return False

    return True


def dogs_bcs():
    """
    Ask user to insert bcs of dog
    Check that right input was provided
    Useing validate_bcs to validate info from user
    validate info and input from user
    append saved value to global variable
    """
    print("Please provide bcs of dog")
    print("Bcs should be a value between 1 and 9")
    while True:
        data_bcs = input("Bcs of dog:")
        saved_bcs = data_bcs

        if validate_bcs(saved_bcs):
            print(f"Bcs of dog provided is {saved_bcs}\n")
            INFO.append(saved_bcs)
            break
    return saved_bcs


def validate_bcs(saved_bcs):
    """
    Function to get body score condition of dog
    Correct value should be from 1 to 9
    Give error to user for invalid value
    """
    try:
        if not (saved_bcs):
            raise ValueError(
                "Field cannot be left blank"
            )
        if int(saved_bcs) <= 0 or int(saved_bcs) >= 10:
            raise ValueError(
                "Please insert value between 1 and 9"
            )

        if saved_bcs.isalpha():
            raise ValueError(
                "Please insert a number"
            )

    except ValueError as error:
        print(f"Invalid data: {error}, please try again.\n")
        return False

    return True


def calcolate_target_weight(INFO):
    """
    Get bcs and weight from dogs_weight and dogs_bcs
    Use correct formula to calcolate correct weight
    Let the user know if dog is under-over or correct weight
    """
    target_weight_part_one = int(INFO[2]) - 5
    target_weight_part_two = 100 + target_weight_part_one * 10
    target_weight_part_three = 100 / target_weight_part_two
    target_weight = float(INFO[1]) * target_weight_part_three
    final_target_weight = format(target_weight, '.2f')
    overweight = target_weight < float(INFO[1])
    underweight = target_weight > float(INFO[1])
    INFO.append(final_target_weight)
    print(f"Ideal weight of dog calcolated is {final_target_weight}")
    if overweight is True:
        print("Your dog is overweight")
        weight_difference = float(INFO[1]) - float(INFO[3])
        print(f"Your dog should lose {format(weight_difference, '.2f')} kg \n")
        wei = "overweight"
    if underweight is True:
        print("Your dog is underweight")
        weight_difference = float(INFO[3]) - float(INFO[1])
        print(f"Your dog should get {format(weight_difference, '.2f')} kg \n")
        wei = "underweight"
    if not underweight and not overweight:
        print("Congratulation! Your dog is in the ideal weight \n")
        wei = "ideal"
        # Calling next function just when dog is in ideal weight
    global WEIGHT
    WEIGHT = wei
    calcolate_rer()


def is_work_dog():
    """
    Life stage factor multiple choice 2 to see which value should be multiplied
    Multiple choice for user and error if value is not correct
    if dog is a work dog
    """
    while True:
        print("Is the dog a work dog?")
        print("Example: police dog, therapy dogs, assistance dogs")
        print("Select one of the following:")
        print("1) Yes\n2) No\n")
        choice = input("")
        if choice == "1":
            print("You selected Yes")
            calcolate_work_dog(LIFE_STAGE)
            break
        if choice == "2":
            print("You selected No")
            life_stage_factor_one(LIFE_STAGE)
            break
        else:
            print('ERROR, Please choose one of the above')
            continue


def calcolate_work_dog(LIFE_STAGE):
    """
    which kind of work the dog does
    """
    print("Work dog selected")
    print("Kind of exercise that dog has daily")
    while True:
        print("Select one of the following:")
        print("1) Light\n2) Moderate\n3) Heavy\n")
        choice = input("")
        if choice == "1":
            x = 2
            print("You selected Light")
            LIFE_STAGE = int(x)
            calcolate_mer(LIFE_STAGE)
            break
        if choice == "2":
            x = 3
            print("You selected Moderate")
            LIFE_STAGE = int(x)
            calcolate_mer(LIFE_STAGE)
            break
        if choice == "3":
            x = 6
            print("You selected Heavy")
            LIFE_STAGE = int(x)
            calcolate_mer(LIFE_STAGE)
            break
        else:
            print('ERROR, Please choose one of the above')
            continue
    return LIFE_STAGE


def calcolate_mer(LIFE_STAGE):
    """
    calcolation based on
    if overweight or underweight calcolate x per ideal weight
    if ideal weight x per weight
    Calcolate mer , using life stage factor and rer
    """
    if WEIGHT == "overweight":  # if overweight
        overweight_mer = float(LIFE_STAGE) * float(INFO[4])
        print(LIFE_STAGE)
        print(overweight_mer)
        mer = overweight_mer
    if WEIGHT == "underweight":
        underweight_mer = float(LIFE_STAGE) * float(INFO[4])
        mer = underweight_mer
    if WEIGHT == "ideal":
        ideal_weight_mer = float(LIFE_STAGE) * float(INFO[4])
        mer = format(ideal_weight_mer, '.2f')
    INFO.append(mer)


def calcolate_rer():
    """
    Calcolate resting energy requirement
    for ideal weight
    rer : calcolatation =  weight^0.75 x 70
    for underweight or overweight
    rer : calcolatation =  ideal weight^0.75 x 70
    taking saved weight to calcolate rer from info_dog
    """
    if WEIGHT == "overweight" or "underweight":
        rer_part_one = float(INFO[3])**0.75
        rer_part_two = rer_part_one * 70
        rer = format(rer_part_two, '.2f')
        print(f"Your dog calcolated rer is {rer} based on his ideal weight\n")
    if WEIGHT == "ideal":
        rer_part_one = float(INFO[1])**0.75
        rer_part_two = rer_part_one * 70
        rer = format(rer_part_two, '.2f')
        print(f"Your dog calcolated rer is {rer} based on his ideal weight\n")
    INFO.append(rer)
    is_work_dog()


def life_stage_factor_one(LIFE_STAGE):
    """
    If ideal weight use weight
    if not in ideal weight use target_weight for calcolation
    Life stage factor multiple choice 1 to see which value should be multiplied
    Multiple choice for user and error if value is not correct
    intact or neutered dog
    """
    while True:
        print("Please answer the following based on life stage of dog:")
        choice = input("1) Neutered\n2) Intact\n3) Definition:\n")
        choice = int(choice)
        if choice == 1:
            x = float(1.6)
            print("You selected Neutered")
            LIFE_STAGE = x
            calcolate_mer(LIFE_STAGE)
            break
        if choice == 2:
            x = float(1.8)
            print("You selected Intact")
            LIFE_STAGE = x
            calcolate_mer(LIFE_STAGE)
            break
        if choice == 3:
            print("\nDefinition:\n")
            print("Neutered = Infertile dog , with no ability to reproduce.\n")
            print("Intact = dog means a dog with intact sexual organs.\n")
            continue
    return LIFE_STAGE


def display_info():
    """
    gave user choice which info would like to be displayed
    info from external sheet file
    after choice loop through element of info chosen to show right column
    validate input
    call choice_calc_end to calcolate calories or end program
    """
    print("Please select argument:\n")
    rows = []
    for row in data:
        rows.append(row)
    i = 1
    for row in rows[0]:
        print(f" {i}) {row}")
        i += 1
    while True:
        choice_topic = input("")
        chosen_topic = choice_topic
        column_vals = gen_info.col_values(chosen_topic)
        column = '\n'.join(column_vals)
        if validate_topic(chosen_topic, column):
            print(column)
            break

    choice_calc_end()


def validate_topic(chosen_topic, column):
    """
    validate user input from display_info and gave error if wrong input
    """
    try:
        if not chosen_topic:
            raise ValueError(
                "Field cannot be left blank"
            )
        if chosen_topic > column:
            raise ValueError(
                "Number selected out of range, please select one of the above"
            )
        if chosen_topic.isalpha():
            raise ValueError(
                "Please insert a number"
            )

    except ValueError as error:
        print(f"Invalid data: {error}, please try again.\n")
        return False

    return True


def choice_calc_end():
    """
    List general info and give another choice to user
    Let user choose if he wants to calcolate calories
    Or is done and do not need anything else
    """
    while True:
        print("\nWould you like to end program ,calcolate calories or continue?")
        print("Please choose one of the following:")
        print(" 1) More info.\n 2) Calcolate calories.\n 3) End program.")
        choice_two = input("")
        if choice_two == "1":
            print("More general information.")
            display_info()
        if choice_two == "2":
            print("Please answer following questions:")
            main()
        if choice_two == "3":
            print("Thank you come back soon.")
            quit()
        else:
            print('ERROR, Please choose one of the above')
            continue


def update_worksheet(info_dog):
    """
    Receives a list of integers to be inserted into a worksheet
    Update the relevant worksheet with the data provided
    """
    worksheet_to_update = profile
    worksheet_to_update.append_row(info_dog)
    print(info_dog)


def summary_info(info_dog):
    """
    get all info of dog saved and show it in a table
    if already saved dog than show all dogs summary
    """


def main():
    """
    main function
    calling all other function here for better structure
    """
    dogs_name()
    dogs_weight()
    dogs_bcs()
    info_dog = INFO
    calcolate_target_weight(info_dog)
    update_worksheet(info_dog)
    summary_info(info_dog)
    quit()


login__or_register()
just_info()
main()
