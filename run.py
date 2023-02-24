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
        print(" A) Get general info.\n B) Calcolate calories.")
        choice = input(" ")
        if choice == "A" or "a":
            print("General info loading.")
        elif choice == "B" or "b":
            print("Please answer the following questions.")
        else:
            print('ERROR, Please choose one of the above')
        break


def general_info():
    """
    List general info and give another choice to user
    Let user choose if he wants to calcolate calories
    Or is done and do not need anything else
    """
    while True:
        print("Example instrucion here.............")
        print("Would you like to end the program or calcolate calories?")
        print("Please choose one of the following:")
        print(" A) Calcolate calories .\n B) End program.")
        choice_two = input("")
        if choice_two == "A" or "a":
            print("Please answer following questions:")
        elif choice_two == "B" or "b":
            print("Thank you come back soon.")
        break


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
            return False

        [int(value) for value in saved_weight]
        if int(saved_weight) <= 0 or int(saved_weight) > 100:
            raise ValueError(
                "Please insert value between 0 and 100"
            )
            return False

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
            return False

        if not values:
            raise ValueError(
                "Field cannot be left blank"
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
            return False

        [int(value) for value in saved_bcs]
        if int(saved_bcs) <= 0 or int(saved_bcs) >= 10:
            raise ValueError(
                "Please insert value between 1 and 9"
            )
            return False

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
    if underweight is True:
        print("Your dog is underweight")
        weight_difference = float(INFO[3]) - int(INFO[1])
        print(f"Your dog should get {format(weight_difference, '.2f')} kg \n")
    if not underweight and not overweight:
        print("Congratulation! Your dog is in the ideal weight \n")
        # Calling next function just when dog is in ideal weight
        life_stage_factor_one()


def calcolate_rer():
    """
    Calcolate resting energy requirement
    rer : calcolatation =  weight^0.75 x 70
    taking saved weight to calcolate rer from info_dog
    """
    rer_part_one = int(INFO[1])**0.75
    rer_part_two = rer_part_one * 70
    rer = format(rer_part_two, '.2f')
    print(f"Your dog calcolated rer is {rer} based on his weight\n")


def life_stage_factor_one():
    """
    If ideal weight
    Life stage factor multiple choice 1 to see which value should be multiplied
    Multiple choice for user and error if value is not correct
    intact or neutered dog
    """
    while True:
        print("Please answer the following based on life stage of dog:")
        choice = input("1) Neutered\n2) Intact\n3) Definition:\n")
        choice = int(choice)
        if choice == 1:
            x = 1.5
            print("You selected Neutered")
            break
        if choice == 2:
            x = 1.7
            print("You selected Intact")
            break
        if choice == 3:
            print("Definition:\n")
            print("Neutered = Infertile dog , with no ability to reproduce.\n")
            print("Intact = dog means a dog with intact sexual organs.\n")
            continue
    life_stage.append(x)
    print(life_stage)


life_stage = []


def calcolate_work_dog():
    print("Work dog selected")
    print("Select one of the following:")
    choice = input("1) Light\n2) Moderate\n3)Heavy\n")
    choice = int(choice)
    while True:
        if choice == 1:
            x = 1.8
            print("You selected Light")
            break
        if choice == 2:
            x = 3.5
            print("You selected Moderate")
            break
        if choice == 3:
            x = 8
            print("You selected Heavy")
            break
    life_stage.append(x)
    print(life_stage)


def life_stage_factor_two():
    """
    If ideal weight
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
            calcolate_work_dog()
            print("You selected Yes")
            break
        if choice == 2:
            x = 1.7
            print("You selected No")
            break
    life_stage.append(x)
    print(life_stage)


def calcolate_mer():
    """
    Calcolate mer , using life stage factor and rer
    if ideal weight then ask for life stage factor
    if dog has to lose weight is rer * 1
    if dog has to gain weight is rer * 1.7
    """


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
    general_info()
    dogs_name()
    dogs_weight()
    dogs_bcs()
    info_dog = INFO
    calcolate_target_weight(info_dog)
    calcolate_rer()
    update_worksheet(info_dog)

    
main()
