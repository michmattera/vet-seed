#  import modules
import os
import random  # use to create random unicode for user
from operator import itemgetter  # use to get right data to display in table
import time  # use to wait specific time before running next function
from time import sleep  # use for slow test
from tabulate import tabulate  # use to display final datas
import gspread  # use to store datas
from google.oauth2.service_account import Credentials  # credentials
from termcolor import colored, cprint   # use to import colors
import art  # use for intro ASCII


SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]


CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('VetSeed')

# import from excel specific sheet and store values in variables
profile = SHEET.worksheet('profile')
dog_datas = profile.get_all_values()
credent = SHEET.worksheet('credentials')
user_data = credent.get_all_values()
gen_info = SHEET.worksheet('general_info')
data = gen_info.get_all_values()

INFO = []  # stores a list from user input(weight-name-bsc-rer-mer)
WEIGHT = ""  # stores saved_weight
LIFE_STAGE = float()  # depending on the life stage different values stored
MER = []  # stores calculated mer
LOG_DET = []  # stores username, password, and Unicode
unicode_list = credent.col_values(3)  # get unicode from 3 columns of credent


def clear_screen():
    '''
    Function for cleaning the screen
    '''
    os.system("clear")


def print_slow(text):
    """
    function to print slow text
    """
    for value in text:    # cycle through the text one character at a time
        print(value, end='', flush=True)  # print one character
        sleep(0.03)
    print()  # go to a new line


def print_slow_art(text):
    """
    function to print slowly just art
    """
    for value in text:    # cycle through the text one character at a time
        print(value, end='', flush=True)  # print one character
        sleep(0.01)
    print()  # go to a new line


def menu():
    """
    first function intro to user
    display art ASCII
    choice: login or create an account
    if login check from a sheet for credentials
    if the right data then login
    if create call a  function to create an account

    """
    art.TITLE = colored(art.TITLE, 'green', attrs=['bold'])
    print_slow_art(art.TITLE)
    art.INTRO = colored(art.INTRO, 'green')
    print_slow(art.INTRO)
    time.sleep(4)
    clear_screen()
    while True:
        print(" Please select one of the following before continue\n")
        print(" 1) Login.\n 2) Create account.\n")
        choice = input("\n")
        if choice == "1":
            clear_screen()
            print("\nInput your login details")
            user = input("Username: \n")
            psw = input("Password: \n")
            uni = input("Unicode: \n")
            try_user = user
            try_psw = psw
            try_uni = uni
            try_det = [try_user, try_psw, try_uni]
            if try_det in user_data:
                clear_screen()
                cprint(f"Welcome back {try_user}\n", 'green')
                INFO.append(try_uni)
                multiple_choice(uni)
                break
            if try_det not in user_data:
                cprint("Information inserted not valid\n", 'red')
                cprint("Please try again\n", 'red')
                continue
        if choice == "2":
            create_username()
        else:
            cprint("Please select one of the above", 'red')
            continue


def multiple_choice(uni):
    """
    multiple choice
    choose between general info, calculate calories,
    display dog's info or end the program
    each choice clears screen and call the right function
    """
    while True:
        time.sleep(2)
        print("\n")
        print(" Please select one of the following before continue\n")
        print(" 1) Get general info.\n 2) Calcolate calories.")
        print(" 3) Show saved dogs\n 4) End program.")
        choice = input("\n")
        if choice == "1":
            print("General info loading.")
            clear_screen()
            display_arguments(uni)
        elif choice == "2":
            clear_screen()
            main()
        elif choice == "3":
            print("Loading saved dogs information ...")
            clear_screen()
            show_info(uni)
        elif choice == "4":
            cprint("Thank you come back soon.", 'blue')
            time.sleep(2)
            clear_screen()
            end_program()
        else:
            cprint('ERROR, Please choose one of the above', 'red')
            continue


def create_username():
    """
    if the user wants to create account , ask the user to create a username
    validate user input with validate_user
    """
    clear_screen()
    while True:
        print("Please insert username")
        print("Username should not be longer than 10 letters\n")
        user = input("Username: \n")
        saved_user = user

        if validate_user(saved_user):
            cprint("Thank you\n", 'green')
            time.sleep(2)
            clear_screen()
            create_password(saved_user)
    return saved_user


def create_password(saved_user):
    """
    after creating the username, ask user to enter the password
    validate user input
    if validate call create_account and stores values
    """
    clear_screen()
    while True:
        print("Please insert password")
        print("Requirements: 5 letters, one number and first capital letter\n")
        psw = input("Password: \n")
        saved_password = psw

        if validate_password(saved_password):
            time.sleep(2)
            clear_screen()
            create_account(saved_password, saved_user)
    return saved_password


def create_account(saved_password, saved_user):
    """
    Create an account, taking saved variables from the following function
    create_username and create_password after validating user inputs
    assign if validate Unicode that user will need to login
    check if Unicode is not already in use, if it is restarted
    save username, password, and Unicode in the external sheet for future login
    asking the user to confirm all data will be saved
    or to change the restart function by asking username and password again
    """
    cprint("Username and password valid\n", 'green')
    while True:
        print("Do you want to confirm? Select:\n 1) Confirm.\n 2) Change")
        choice = input("\n")
        if choice == "1":
            unicode = (random.randint(100, 5000))
            while str(unicode) in unicode_list:
                unicode = (random.randint(100, 5000))
            LOG_DET.append(saved_user)
            LOG_DET.append(saved_password)
            LOG_DET.append(unicode)
            INFO.append(unicode)
            uni = unicode
            clear_screen()
            cprint(f"Unicode assign to you : {unicode}\n", 'blue')
            cprint("Please save unicode.\n", 'blue')
            cprint("Unicode required to login\n", 'blue')
            time.sleep(2)
            are_you_ready(uni)
            return unicode
        if choice == "2":
            create_username()
        else:
            cprint('ERROR, Please choose one of the above', 'red')
            continue


def are_you_ready(uni):
    """
    The choice of the user after assigning Unicode before going to the main menu
    be sure that user saved Unicode before going on
    """
    while True:
        print("Are you ready to go to main menu?\n")
        print("If you saved Unicode")
        print("Please type yes to continue")
        choice = input("\n")
        if choice == "yes":
            cprint("Thank you", 'green')
            print_slow("Loading...")
            time.sleep(2)
            clear_screen()
            multiple_choice(uni)
        else:
            cprint('ERROR, Please type YES to continue', 'red')
            continue


def validate_user(user):
    """
    check user value from create_account
    check if the value is there
    check if is no longer than 10 letters
    raise an error if the wrong input
    """
    try:
        if len(user) > 10:
            raise ValueError(
                f"Max length of name is 10 letters you gave {len(user)}"
            )
        if not user:
            raise ValueError(
                "Field cannot be empty"
            )

    except ValueError as error:
        cprint(f"Invalid data: {error}, please try again.\n", 'red')
        return False
    return True


def validate_password(password):
    """
    check user value from create_account
    check if the value is there
    check if is long at least 5 letters
    if the first is a capital letter
    and if there is at least one number
    raise an error if otherwise
    """
    uppercase_count = 0
    flag = False
    try:
        if len(password) < 5:
            raise ValueError(
                f"Min length of password is 5 letters you gave {len(password)}"
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
            if i.isdigit():
                flag = True
                break
        if flag:
            cprint("Thank you", 'green')
        else:
            raise ValueError(
                "At least one number required"
            )

    except ValueError as error:
        cprint(f"Invalid data: {error}, please try again.\n", 'red')
        return False
    return True


def dogs_name():
    """
    ask the user to insert the name of the dog
    validate info and input from the user
    append saved value to a global variable
    """
    uni = INFO[0]
    print("Please answer the following questions.\n")

    print("Please insert first name of dog")
    print("Example: Bob\n")
    print("max characters accepted are 10\n")
    while True:
        data_name = input("Name of dog: \n")
        saved_name = data_name

        if validate_name(saved_name):
            cprint("Valid name", 'green')
            cprint(f"Name of dog provided is {saved_name}\n", 'green')
            time.sleep(2)
            clear_screen()
# https://stackoverflow.com/questions/850795/different-ways-of-clearing-lists
# link and info used to clear the list
            del INFO[:]
            INFO.append(uni)
            INFO.append(saved_name)
            break
    return saved_name


def validate_name(saved_name):
    """
    Validate name
    gave an error if more than 10 letters
    gave an error if a number instead of a letter was given
    if more than one world was given
    raise an error if empty space
    """
    try:
        if len(saved_name) > 10:
            raise ValueError(
                f"Max length of name is 10 letters you gave {len(saved_name)}"
            )

        if not saved_name:
            raise ValueError(
                "Field cannot be left blank"
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
    Ask the user to insert the weight of the dog
    Check that the right input was provided
    validate info and input from the user
    append saved value to a global variable
    """
    print("Please provide weight of dog")
    print("Please provide exact weight from 0 to 100 kg")
    while True:
        data_weight = input("Weight of dog: \n")
        saved_weight = data_weight

        try:
            float(saved_weight)
            if validate_weight(saved_weight):
                cprint("Valid weight", 'green')
                cprint(f"Weight of dog provided is {saved_weight}\n", 'green')
                time.sleep(2)
                clear_screen()
                INFO.append(saved_weight)
                break

        except Exception as ex:
            cprint('ERROR, data inserted invalid, please try again\n', 'red')
            continue
    return saved_weight


def validate_weight(saved_weight):
    """
    Validate weight
    check if the value was between 0 and 100
    check if values were not a letter
    give an error if invalid value or empty
    """
    try:
        if not saved_weight:
            raise ValueError(
                "Field cannot be left blank"
            )

        if float(saved_weight) <= 0 or float(saved_weight) > 100:
            raise ValueError(
                "Please insert a value between 0 and 100"
            )

    except ValueError as error:
        cprint(f"Invalid data: {error}, please try again.\n", 'red')
        return False

    return True


def dogs_bcs():
    """
    Ask the user to insert bcs of the dog
    Check that the right input was provided
    Using validate_bcs to validate info from user
    validate info and input from the user
    append saved value to a global variable
    """
    print("Please provide bcs of dog")
    print("Bcs should be a value between 1 and 9")
    while True:
        data_bcs = input("Bcs of dog: \n")
        saved_bcs = data_bcs

        try:
            int(saved_bcs)
            if validate_bcs(saved_bcs):
                cprint("Valid Bcs", 'green')
                cprint(f"Bcs of dog provided is {saved_bcs}\n", 'green')
                time.sleep(2)
                clear_screen()
                INFO.append(saved_bcs)
        except Exception as ex:
            cprint('Sorry, that is not a whole number, please try again\n', 'red')
            continue
            #break
    return saved_bcs


def validate_bcs(saved_bcs):
    """
    Function to get body score condition of the dog
    The correct value should be from 1 to 9
    Give an error to the user for an invalid value
    """
    try:
        if not (saved_bcs):
            raise ValueError(
                "Field cannot be left blank"
            )
        if int(saved_bcs) <= 0 or int(saved_bcs) >= 10:
            raise ValueError(
                "Please insert a value between 1 and 9"
            )

    except ValueError as error:
        cprint(f"Invalid data: {error}, please try again.\n", 'red')
        return False

    return True


def calcolate_target_weight(INFO):
    """
    Get BCS and weight from dogs_weight and dogs_bcs
    Use the correct formula to calculate the correct weight
    Let the user know if dog is under-weight, over-weight or correct weight
    call function to calculate rer based on the weight of the dog
    """
    target_weight_part_one = int(INFO[3]) - 5
    target_weight_part_two = 100 + target_weight_part_one * 10
    target_weight_part_three = 100 / target_weight_part_two
    target_weight = float(INFO[2]) * target_weight_part_three
    final_target_weight = format(target_weight, '.2f')
    overweight = target_weight < float(INFO[2])
    underweight = target_weight > float(INFO[2])
    INFO.append(final_target_weight)
    print(f"Ideal weight of dog calculated is {final_target_weight}")
    clear_screen()
    print_slow("Calculating....\n")
    time.sleep(2)
    if overweight is True:
        cprint("Your dog is overweight", 'yellow')
        weight_diff = float(INFO[2]) - float(INFO[4])
        cprint(f"Dog should lose {format(weight_diff, '.2f')} kg\n", 'yellow')
        wei = "overweight"
    if underweight is True:
        cprint("Dog is underweight", 'yellow')
        weight_diff = float(INFO[4]) - float(INFO[2])
        cprint(f"Dog should get {format(weight_diff, '.2f')} kg\n", 'yellow')
        wei = "underweight"
    if not underweight and not overweight:
        cprint("Congratulation! Your dog is in the ideal weight \n", 'green')
        wei = "ideal"
    global WEIGHT
    WEIGHT = wei
    calcolate_rer()


def is_work_dog():
    """
    Life stage factor multiple choice 2 to see which value should be multiplied
    Multiple choice for user and error if the value is not correct
    if the dog is a working dog
    """
    while True:
        print_slow("To calculate precise calories per day")
        print_slow("please answer the following:\n")
        print("Is the dog a work dog?\n")
        print("Example: police dog, therapy dogs, assistance dogs\n")
        print("Select one of the following:")
        print("1) Yes\n2) No\n")
        choice = input("\n")
        if choice == "1":
            cprint("You selected Yes", 'blue')
            time.sleep(2)
            clear_screen()
            calcolate_work_dog(LIFE_STAGE)
            break
        if choice == "2":
            cprint("You selected No", 'blue')
            time.sleep(2)
            clear_screen()
            life_stage_factor_one(LIFE_STAGE)
            break
        else:
            print('ERROR, Please choose one of the above')
            continue


def calcolate_work_dog(LIFE_STAGE):
    """
    which kind of work the dog does
    based on choice calculate final calories to provide the dog
    """
    print("Work dog selected")
    print("Kind of exercise that dog has daily")
    while True:
        print("Select one of the following:")
        print("1) Light\n2) Moderate\n3) Heavy\n")
        choice = input("\n")
        clear_screen()
        if choice == "1":
            x = 2
            cprint("You selected Light", 'blue')
            LIFE_STAGE = int(x)
            calcolate_mer(LIFE_STAGE)
            break
        if choice == "2":
            x = 3
            cprint("You selected Moderate", 'blue')
            LIFE_STAGE = int(x)
            calcolate_mer(LIFE_STAGE)
            break
        if choice == "3":
            x = 6
            cprint("You selected Heavy", 'blue')
            LIFE_STAGE = int(x)
            calcolate_mer(LIFE_STAGE)
            break
        else:
            print('ERROR, Please choose one of the above')
            continue
    return LIFE_STAGE


def calcolate_mer(LIFE_STAGE):
    """
    calculation based on
    if overweight or underweight calculate x per ideal weight
    if ideal weight x per weight
    Calculate mer , using life stage factor and rer
    """
    if WEIGHT == "overweight":  # if overweight
        overweight_mer = float(LIFE_STAGE) * float(INFO[5])
        mer = overweight_mer
        cprint("Calcolating calories to help dog lose weight...\n", 'blue')
        cprint(f"Kcal {mer}", 'yellow')
    if WEIGHT == "underweight":
        underweight_mer = float(LIFE_STAGE) * float(INFO[5])
        mer = underweight_mer
        cprint("Calcolating calories to help dog get weight...\n", 'blue')
        cprint(f"Kcal {mer}", 'yellow')
    if WEIGHT == "ideal":
        ideal_weight_mer = float(LIFE_STAGE) * float(INFO[5])
        mer = ideal_weight_mer
        cprint("Please continue to give dog daily...\n")
        cprint(f"Kcal {mer}", 'green')
    final_mer = format(mer, '.2f')
    INFO.append(final_mer)


def calcolate_rer():
    """
    Calculate resting energy requirement
    for ideal weight
    rer : calculation =  weight^0.75 x 70
    for underweight or overweight
    rer : calculation =  ideal weight^0.75 x 70
    taking saved weight to calculate rer from info_dog
    calling function to see if the dog is a working dog
    """
    if WEIGHT == "overweight" or "underweight":
        rer_part_one = float(INFO[4])**0.75
        rer_part_two = rer_part_one * 70
        rer = format(rer_part_two, '.2f')
        cprint(f"RER calculated : {rer} based on his ideal weight\n", 'yellow')
    if WEIGHT == "ideal":
        rer_part_one = float(INFO[2])**0.75
        rer_part_two = rer_part_one * 70
        rer = format(rer_part_two, '.2f')
        cprint(f"RER calcolated : {rer} based on his weight\n", 'green')
    INFO.append(rer)
    time.sleep(2)
    is_work_dog()


def life_stage_factor_one(LIFE_STAGE):
    """
    If the ideal weight use the weight
    if not in ideal weight use target_weight for calculation
    Life stage factor multiple choice 1 to see which value should be multiplied
    Multiple choice for user and error if the value is not correct
    intact or neutered dog
    return value to store in a global variable
    """
    while True:
        print("Please answer the following based on life stage of dog:\n")
        cprint("Press d for definition\n", 'blue')
        choice = input("1) Neutered\n2) Intact\n\n")
        if choice == "1":
            x = float(1.6)
            clear_screen()
            cprint("You selected Neutered", 'blue')
            time.sleep(2)
            LIFE_STAGE = x
            calcolate_mer(LIFE_STAGE)
            break
        if choice == "2":
            x = float(1.8)
            clear_screen()
            cprint("You selected Intact", 'blue')
            time.sleep(2)
            LIFE_STAGE = x
            calcolate_mer(LIFE_STAGE)
            break
        if choice == "d":
            print("\nDefinition: \n")
            print_slow("Neutered = Infertile dog ,no ability to reproduce.\n")
            print_slow("Intact = dog means a dog with intact sexual organs.\n")
            clear_screen()
            continue
        else:
            cprint(
                "Please select one of the above", 'red'
            )
            continue
    return LIFE_STAGE


def display_arguments(uni):
    """
    gave the user a choice between arguments to show
    info from external sheet file
    for each row than print all column
    validate input to be an integer
    if not integer gave error
    if integer than calling display_chosen_topic
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
        choice_topic = input("\n")
        try:
            int(choice_topic)
        except Exception as ex:
            cprint('Sorry, that is not a number, please try again\n', 'red')
            continue
        if int(choice_topic) in [1, 2, 3, 4, 5, 6, 7]:
            display_chosen_topic(choice_topic, uni)
        else:
            cprint("Number selected out of range, please try again", 'red')
            continue


def display_chosen_topic(choice_topic, uni):
    """
    for each chosen topic print all rows of that column
    than validate if user input is valid
    if is in range than print column
    otherwise error
    after printing right column gave user again multiple choice
    to decide what he would like to do
    """
    column_vals = gen_info.col_values(choice_topic)
    column = '\n\n'.join(column_vals)
    time.sleep(3)
    clear_screen()
    print_slow(column)
    multiple_choice(uni)


def update_worksheet(info_dog):
    """
    Receives a list of integers to be inserted into a worksheet
    Update the relevant worksheet with the data provided
    call again function to give the user choice of what he wants to do
    """
    info_dog = INFO
    print_slow("Updating datas...\n")
    time.sleep(2)
    worksheet_to_update = profile
    worksheet_to_update.append_row(info_dog)
    uni = info_dog[0]
    cprint("All datas updated and saved\n", 'green')
    time.sleep(2)
    clear_screen()
    multiple_choice(uni)


def extract(new_dog_datas):
    """
    extract the first item in dog-data list of lists
    """
    new_dog_datas = profile.get_all_values()
    return list(map(itemgetter(0), new_dog_datas))


def show_info(uni):
    """
    get again info from dog_datas updated
    call function Extract to extract indexes of all rows in the list
    stringify uni so from create acc does not return int
    for loop to find in indexes list uni
    and then for all uni found print it in tabulate
    if not uni found then print an error message
    calling function to give the user multiple choice

    """
    print_slow("Finding dogs....\n")
    time.sleep(1)
    new_dog_datas = profile.get_all_values()
    ind_list = extract(new_dog_datas)
    str_u = str(uni)
    ind_uni = [index for (index, item) in enumerate(ind_list) if item == str_u]
    i = 0
    test = []
    for i in ind_uni:
        test.append(new_dog_datas[i])
        i += 1
    cprint(tabulate(
        test, headers=["Unicode", "Name", "Weight", "BCS",
                       "Ideal weight", "RER", "MER"],
        tablefmt='fancy_grid'), 'blue')
    if not ind_uni:
        cprint("No dogs saved", 'red')
        cprint("To save dog please calculate calories\n", 'red')
    time.sleep(2)
    multiple_choice(uni)


def end_program():
    """
    end program, thank the user, update all information
    updating info user here so also if there is no calculation but just
    general info consulted info_user is saved
    """
    info_user = LOG_DET
    worksheet_to_update = credent
    worksheet_to_update.append_row(info_user)
    time.sleep(2)
    quit()


def main():
    """
    main function
    calling all other functions here for better structure
    """
    dogs_name()
    dogs_weight()
    dogs_bcs()
    info_dog = INFO
    calcolate_target_weight(info_dog)
    update_worksheet(info_dog)


menu()
main()
