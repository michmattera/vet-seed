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

INFO = []  # stores a list from user input(weight-name-bsc)
WEIGHT = ""
LIFE_STAGE = float()
MER = []


def just_info():
    """
    give user choice
    Create function for introduction of topic
    choose between get just general information 
    or go and calcolate dog's per day calories
    """
    print("Welcome to VetSeed, program to authomate data for all vets.")
    while True:
        print("Please choose what would you like to know:\n")
        print("Do you want to?")
        print(" 1) Get general info.\n 2) Calcolate calories.")
        choice = input("")
        if choice == "1":
            print("General info loading.")
            general_info()
        elif choice == "2":
            print("Please answer the following questions.")
            dogs_name()
        else:
            print('ERROR, Please choose one of the above')
            continue


def general_info():
    """
    List general info and give another choice to user
    Let user choose if he wants to calcolate calories
    Or is done and do not need anything else
    """
    print("Example instrucion here.............")
    print("Would you like to end the program or calcolate calories?")
    print("Please choose one of the following:")
    print(" 1) Calcolate calories .\n 2) End program.")
    choice_two = input("")
    if choice_two == "1":
        print("Please answer following questions:")
        dogs_name()
    if choice_two == "2":
        print("Thank you come back soon.")
        quit()


def dogs_name():
    """
    define goal of program
    ask user to insert name of dog
    validate info and input from user
    append saved value to global variable
    """
    #  data = profile.get_all_values()
    # print(data)
    while True:
        print("Please insert first name of dog")
        print("Example: Bob\n")

        data_name = input("Name of dog:\n")
        saved_name = data_name

        if validate_info(saved_name):
            print("Thank you")
            print(f"Name of dog provided is {saved_name}\n")
            INFO.append(saved_name)
            print(INFO)
            break
    return saved_name


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

        if int(saved_weight) <= 0 or int(saved_weight) > 100:
            raise ValueError(
                "Please insert value between 0 and 100"
            )

    except ValueError as error:
        print(f"Invalid data: {error}, please try again.\n")
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

        if not values:
            raise ValueError(
                "Field cannot be left blank"
            )

    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")
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
        if not saved_bcs:
            raise ValueError(
                "Field cannot be left blank"
            )
        if int(saved_bcs) <= 0 or int(saved_bcs) >= 10:
            raise ValueError(
                "Please insert value between 1 and 9"
            )
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")
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
    target_weight = int(INFO[1]) * target_weight_part_three
    final_target_weight = format(target_weight, '.2f')
    overweight = target_weight < int(INFO[1])
    underweight = target_weight > int(INFO[1])
    INFO.append(final_target_weight)
    print(f"Ideal weight of dog calcolated is {final_target_weight}")
    if overweight is True:
        print("Your dog is overweight")
        weight_difference = int(INFO[1]) - float(INFO[3])
        print(f"Your dog should lose {format(weight_difference, '.2f')} kg \n")
        wei = "overweight"
    if underweight is True:
        print("Your dog is underweight")
        weight_difference = float(INFO[3]) - int(INFO[1])
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
        print("Select one of the following:")
        choice = input("1) Yes\n2) No\n")
        choice = int(choice)
        if choice == 1:
            print("You selected Yes")
            calcolate_work_dog(LIFE_STAGE)
            break
        if choice == 2:
            print("You selected No")
            life_stage_factor_one(LIFE_STAGE)
            break


def calcolate_work_dog(LIFE_STAGE):
    """
    which kind of work the dog does
    """
    print("Work dog selected")
    print("Kind of exercise that dog has daily")
    print("Select one of the following:")
    choice = input("1) Light\n2) Moderate\n3) Heavy\n")
    choice = int(choice)
    while True:
        if choice == 1:
            x = int(2)
            print("You selected Light")
            LIFE_STAGE = x
            calcolate_mer(LIFE_STAGE)
            break
        if choice == 2:
            x = int(3)
            print("You selected Moderate")
            LIFE_STAGE = x
            calcolate_mer(LIFE_STAGE)
            break
        if choice == 3:
            x = int(6)
            print("You selected Heavy")
            LIFE_STAGE = x
            calcolate_mer(LIFE_STAGE)
            break
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


def update_worksheet(info_dog):
    """
    Receives a list of integers to be inserted into a worksheet
    Update the relevant worksheet with the data provided
    """
    worksheet_to_update = SHEET
    worksheet_to_update.append_row(info_dog)
    print(info_dog)


def main():
    """
    main function
    calling all other function here for better structure
    """
    just_info()
    dogs_weight()
    dogs_bcs()
    info_dog = INFO
    calcolate_target_weight(info_dog)
    update_worksheet(info_dog)


main()
