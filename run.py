#  import module
import os
import sys
# importing the random module
import random
from operator import itemgetter
from tabulate import tabulate
import gspread
from google.oauth2.service_account import Credentials
from termcolor import colored, cprint
import art


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
credent = SHEET.worksheet('credentials')
gen_info = SHEET.worksheet('general_info')
data = gen_info.get_all_values()
user_data = credent.get_all_values()
dog_datas = profile.get_all_values()
INFO = []  # stores a list from user input(weight-name-bsc)
WEIGHT = ""  # stores saved_weight
LIFE_STAGE = float()  # depending on life stage different values stored
MER = []  # stores calcolated mer and after append everything to profile
LOG_DET = []  # stores username and password from user input


def clearScreen():
    '''
    Function for cleaning the cli screen
    '''
    os.system("clear")


def menu(dog_datas):
    """
    Choice to user to login, create an account or gen info
    """
    art.TITLE = colored(art.TITLE, 'green', attrs=['bold'])
    cprint(art.TITLE)
    art.INTRO = colored(art.INTRO, 'green')
    cprint(art.INTRO)
    while True:
        print(" Please select one of the following before continue\n")
        print(" 1) Login.\n 2) Create account.\n")
        choice = input("")
        if choice == "1":
            print("\nInput your login details")
            user = input("Username: ")
            psw = input("Password: ")
            uni = input("Unicode: ")
            try_user = user
            try_psw = psw
            try_uni = uni
            try_det = [try_psw, try_user, try_uni]
            if try_det in user_data:
                cprint(f"welcome {try_user}", 'green')
                INFO.append(try_uni)
                show_info(uni, dog_datas)
                break
            if try_det not in user_data:
                cprint("Please try again\n", 'red')
                continue
        if choice == "2":
            create_username()
        else:
            cprint("Please select one of the above", 'red')
            clearScreen()
            continue


def create_username():
    """
    Create account , asking user to enter username
    validate user from input 
    """
    while True:
        print("Please insert username")
        print("Username should not be longer than 10 letters\n")
        user = input("Username: ")
        saved_user = user

        if validate_user(saved_user):
            print("Thank you\n")
            create_password(saved_user)
    return saved_user


def create_password(saved_user):
    """
    Create account , asking user to enter username
    validate user from input 
    """
    while True:
        print("Please insert password")
        print("Requirements: 5 letters, one number and first capital letter\n")
        psw = input("Password: ")
        saved_password = psw

        if validate_psw(saved_password):
            print("Thank you")
            create_account(saved_password, saved_user)
    return saved_password


def create_account(saved_password, saved_user):
    """
    Create account , taking saved variable from following function
    create_username and create_password after validate the user inputs
    save username and password in external sheet for future login
    """
    while True:

        cprint("Username and password valid\n", 'green')
        print("Do you want to confirm? Select:\n 1) Confirm.\n 2) Change")
        choice = input("")
        if choice == "1":
            unicode = (random.randint(0 ,100000))
            LOG_DET.append(saved_user)
            LOG_DET.append(saved_password)
            LOG_DET.append(unicode)
            INFO.append(unicode)
            print(LOG_DET)
            cprint(f"Unicode assign to you : {unicode}", 'blue')
            cprint("Please save unicode. Unicode required to login\n", 'blue')
            print("Thank you all information will be saved in your account")
            just_info()
            return unicode
        if choice == "2":
            create_username()


def validate_user(user):
    """
    check user value from create_account
    check if value is there
    check if is no longer than 10 letters
    """
    try:
        if len(user) > 10:
            raise ValueError(
                f"Max lenght of name is 10 letters you gave {len(user)}"
            )
        if not user:
            raise ValueError(
                "Field cannot be empty"
            )

    except ValueError as error:
        cprint(f"Invalid data: {error}, please try again.\n", 'red')
        return False
    return True


def validate_psw(password):
    """
    check user value from create_account
    check if value is there
    check if is no longer than 10 letters
    """
    uppercase_count = 0
    try:
        if len(password) < 5:
            raise ValueError(
                f"Min lenght of password is 5 letters you gave {len(password)}"
            )
        if not password:
            raise ValueError(
                "Field cannot be empty"
            )
        for i in password:
            if i.isupper():
                uppercase_count += 1
            if uppercase_count == 0:
                raise ValueError(
                    "First letter required capital letter"
                )
        for i in password:
            if i not in "0123456789":
                raise ValueError(
                    "At least one number required"
                )

    except ValueError as error:
        cprint(f"Invalid data: {error}, please try again.\n", 'red')
        return False
    return True


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
            clearScreen()
            display_info()
        elif choice == "2":
            print("Please answer the following questions.")
            clearScreen()
            main()
        else:
            cprint('ERROR, Please choose one of the above', 'red')
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
            cprint(f"Name of dog provided is {saved_name}\n", 'green')
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
        cprint(f"Invalid data: {error}, please try again.\n", 'red')
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
            cprint(f"Weight of dog provided is {saved_weight}\n", 'green')
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
        cprint(f"Invalid data: {error}, please try again.\n", 'red')
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
            cprint(f"Bcs of dog provided is {saved_bcs}\n", 'green')
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
        cprint(f"Invalid data: {error}, please try again.\n", 'red')
        return False

    return True


def calcolate_target_weight(INFO):
    """
    Get bcs and weight from dogs_weight and dogs_bcs
    Use correct formula to calcolate correct weight
    Let the user know if dog is under-over or correct weight
    """
    target_weight_part_one = int(INFO[3]) - 5
    target_weight_part_two = 100 + target_weight_part_one * 10
    target_weight_part_three = 100 / target_weight_part_two
    target_weight = float(INFO[2]) * target_weight_part_three
    final_target_weight = format(target_weight, '.2f')
    overweight = target_weight < float(INFO[2])
    underweight = target_weight > float(INFO[2])
    INFO.append(final_target_weight)
    print(f"Ideal weight of dog calcolated is {final_target_weight}")
    if overweight is True:
        cprint("Your dog is overweight", 'yellow')
        weight_difference = float(INFO[2]) - float(INFO[4])
        cprint(f"Your dog should lose {format(weight_difference, '.2f')} kg\n", 'yellow')
        wei = "overweight"
    if underweight is True:
        cprint("Your dog is underweight", 'yellow')
        weight_difference = float(INFO[4]) - float(INFO[2])
        cprint(f"Your dog should get {format(weight_difference, '.2f')} kg\n", 'yellow')
        wei = "underweight"
    if not underweight and not overweight:
        cprint("Congratulation! Your dog is in the ideal weight \n", 'green')
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
            clearScreen()
            calcolate_work_dog(LIFE_STAGE)
            break
        if choice == "2":
            print("You selected No")
            clearScreen()
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
        overweight_mer = float(LIFE_STAGE) * float(INFO[5])
        print(LIFE_STAGE)
        print(overweight_mer)
        mer = overweight_mer
    if WEIGHT == "underweight":
        underweight_mer = float(LIFE_STAGE) * float(INFO[5])
        mer = underweight_mer
    if WEIGHT == "ideal":
        ideal_weight_mer = float(LIFE_STAGE) * float(INFO[5])
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
        rer_part_one = float(INFO[4])**0.75
        rer_part_two = rer_part_one * 70
        rer = format(rer_part_two, '.2f')
        cprint(f"Your dog calcolated rer is {rer} based on his ideal weight\n", 'blue')
    if WEIGHT == "ideal":
        rer_part_one = float(INFO[2])**0.75
        rer_part_two = rer_part_one * 70
        rer = format(rer_part_two, '.2f')
        cprint(f"Your dog calcolated rer is {rer} based on his weight\n", 'blue')
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
        cprint(f"Invalid data: {error}, please try again.\n", 'red')
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
            clearScreen()
            display_info()
        if choice_two == "2":
            print("Please answer following questions:")
            clearScreen()
            main()
        if choice_two == "3":
            print("Thank you come back soon.")
            clearScreen()
            quit()
        else:
            cprint('ERROR, Please choose one of the above', 'red')
            continue


def update_worksheet(info_dog, info_user):
    """
    Receives a list of integers to be inserted into a worksheet
    Update the relevant worksheet with the data provided
    """
    print("Updating  datas...")
    worksheet_to_update = profile
    worksheet_to_update.append_row(info_dog)
    print(info_dog)
    worksheet_to_update = credent
    worksheet_to_update.append_row(info_user)
    print(info_user)


def Extract(dog_datas):
    """
    extract first item in dog-datas list of lists
    """
    return list(map(itemgetter(0), dog_datas))


def show_info(uni, dog_datas):
    """
    get all info of dog saved and show it in a table
    using index from function Extract
    if already saved dog than show all dogs summary
    """
    test = Extract(dog_datas)
    new_test = [index for (index, item) in enumerate(test) if item == uni]
    i = 0
    test = []
    for i in new_test:
        test.append(dog_datas[i])
        print(dog_datas[i])
        i += 1
    print(test)

    cprint(tabulate(
        test, headers=["Unicode", "Name", "Weight", "BCS",
        "Ideal weight", "RER", "MER"],
        tablefmt='fancy_grid'), 'blue')


def main():
    """
    main function
    calling all other function here for better structure
    """
    dogs_name()
    dogs_weight()
    dogs_bcs()
    info_dog = INFO
    info_user = LOG_DET
    calcolate_target_weight(info_dog)
    update_worksheet(info_dog, info_user)
    show_info(uni, dog_datas)
    quit()


menu(dog_datas)
just_info()
main()
