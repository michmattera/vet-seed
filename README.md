# **Vet Seed**


![vet Seed Mockup Images](/assets/images/read-me-images/)

[View the live project here](https://vet-seed.herokuapp.com/)
     

## **Table of contents**
***
1. [Introduction](#introduction)
2. [UX](#ux)
    1. [Ideal User Demographic](#ideal-user-demographic)
    2. [User Goals](#user-goals) 
3. [Development Planes](#development-planes)
4. [Features](#features)  
    1. [General Features](#general-features)
    2. [Future features](#future-features)
5. [Design](#design)
6. [Issues and Bugs](#issues-and-bugs)
7. [Technology Used](#technology-used)
    1. [Languages Used](#languages-used)
    2. [External Programs-Website Used](#external-programs-website-used)
8. [Testing](#testing)
9. [Deployment](#deployment)
10. [Credits](#credits)
    1. [Content](#content)
    1. [Code](#code)
11. [Acknowledgements](#acknowledgements)


## **Introduction**
This is a back-end program for veterinarians to do the following:

- Calcolate and save data of subjects (in this case dogs).
- Calcolate if the dog is underweight, overweight or in ideal weight.
- Calcolate as well calories per day that dog should take based on weight and life stage.
- Get general information about dogs.
- Be able to save and have summary of all dogs inserted and saved when login in the account.

The developer wanted to address a real-every-day problem such as calcolate how many calories per day a dog should get based on different factors.

This is a program created for the third of five Milestone projects required to complete the Diploma in Software development (eCommerce Applications) program at **Code Institute**.
The main requirement of this project is to use  **PYTHON** as the main technology. 

## **UX**

### Ideal User demographic

The ideal user demographic for this program are:
- Veterinarians
- People with basic information on BCS to calculate calories per day for their dog

### User goals

The developer divided user goals into the following categories:
1. New user
2. Old user


**New user** 

The main goals are the following:

- Understand straight away what this program can offer
- Be able to create an account
- Get general information on dogs
- Be able to calculate if my dog is overweight, underweight, or ideal weight
- Calculate which one should be the ideal weight for my dog
- Calculate how many calories per day I should give my dog
- See the summary of the calculation in  a table or a file

**Old user** 

The main goals are the following:

- Be able to log in without creating another account
- Calculate another dog's calories and ideal weight
- Be able to have a summary of all dogs already inserted
- Read general info again if forget something

[Back to top ⇧](#Vet-Seed)

## Development Planes

Project purpose:

To build a command-line application that allows users to manage a common dataset about a particular domain.

The vet application was chosen by the developer for the personal interest of the developer in dogs, and to try and create something useful for an everyday task to address a specific target audience. 

Development planes were made in the following order:
- Strategy
- Scope
- Structure
- Skeleton

### Strategy

Used to determine developer goals and user needs.

Chosen target audience: 

1. Veterinarian 
2. People with basic vet information

#### Developer Goals

The developer goals were the following:
- Create an application that could pass through validators without error
- Address an everyday need and try to simplify human tasks using language learned
- Present the application in a clean and easy-to-understand manner
- Try to give even if simple good UX experience

#### User needs

User needs were the following:
- Calculate if a dog is under, over, or ideal weight
- Calculate how many calories to give to the dog based on the weight
- Have visual effect if wrong or right input inserted
- Summary at the end of the program with all information displayed
- Few questions to simplify the process
- After each section choose to end the program

The developer has to get the following information about the user:
- Username
- Password
- Unicode ( just for login )


 When a username and password are created and validated, a random number called *Unicode* will be assigned to a user.

The user will have to save this number to login.


The developer has to get the following information about the dog:
- Name
- Weight
- BCS (Body Score condition)
- Life Stage


### Scope

Now that we have established the goals of the program we can deduce the necessary features:

1. Multiple choice for the user to let him decide what he would like to do
2. Inputs to insert required data
3. Color effect on right and wrong values inserted
4. Message user frequently based on the process and the values given
5. Calculate the final calories per day to give the dog
6. Calculate difference between weight an ideal weight
7. Table to insert at the end of the program for a summary of values provided and calculated
8. Saved user data in an external sheet
9. Save dog's data to be able to access it when the user login

### Structure

Structure for the application was made using [Canva](https://www.canva.com/ "Link to Canva").

Firstly the developer searched all information online to see how to calculate everything and create a basic structure.

With the information found then she created a formulas chart.

<details>
<summary>Formulas for flowchart</summary>
    
![Formulas](assets/images/scheme-formulas.png)

</details> 

Then the developer creates a structural map based on importance and on how to calculate everything.


The structure was then divided in two main sections:
1. General info = Where the user will just get information
2. Main section = Where the user will insert data and get back the result

<details>
<summary>Map structure</summary>
    
![Map structure](assets/images/structure-map.png)

</details> 

The map structure was changed slightly, adding the multiple-choice possibility for the user to show saved dogs in table.

[Back to top ⇧](#Vet-Seed)


## Features

### General Features

- **General section** = User will get general information and advice on dogs based on weight, BCS, and life stage.
- **Input**:
    1. **Name** = Name of dog ( max 10 letters )
    2. **Weight** = Weight of the dog measured at the moment ( from 0 to 100 kg)
    3. **BCS** = 0 to 9 ( 9 scale BCS )
    4. **Life Stage** = Depending on the following criteria:
        - Working dog = Exercise( Light: 2 - Moderate: 4 - Heavy: 6)
        - No working dog = If the dog ( Intact: 1.8 - Neutered: 1.6)
        - Ideal, over or underweight = If a dog ( Ideal weight: life-stage * weight - Over/Underweight: life-stage * ideal weight)
- **Calculation**:
    1. **Ideal weight** = Based on BCS and weight
    2. **Calories** = How many calories per day should the dog get based on ideal weight and life stage.
- **Save data** = All data inserted from the user were then saved in an external google sheet.
- **Table** = Summary table at the end of the application with all data inserted from the user and conclusion.
- **Multiple choice** = Used mainly to change section from main to general and vice versa. Or to restart and end the program.
- **Visual effect** = To give users a better UX experience.

### Future features

Due to limited resources (time constraints, skills of the developer at the moment, and other reasons), some features were not implemented.

1. Be able to access old dog's data with login and be able to update already saved data with new values. Having updated data showed as well in the final summary.

## Design

The design of a command line application is usually very simple. The developer though decided that for a better UX experience would be implemented:
- **Colors**:
    1. **Red** = Would be assigned to a wrong value inserted by the user to help him visualize the error.
    2. **Green** = Would be assigned to the correct value inserted by the user to help him visualize that no error was given when data are saved correctly and intro and ASCII art.
    3. **Blue** = Would be assigned to general information and return calculation to highlight it from other text.
    4. **Yellow** = Would be assigned to data that indicate important data, such as if the dog is underweight or overweight.
- **Space** = More space between sections and important sentences to highlight the right information.
- **Time** = Between different functions and calculations for better UX.
- **Clear** = Functionality to eliminate section by section to not overwhelm the user with information.
- **Intro design** = Intro design using ASCII art, to give a better user experience.
- **Tabulate** = Fancy tabulate in blue, to give a better user experience when showing saved information to the user.

## Issues and bugs

The developer found different issues and bugs during the creation of the application, the main issues and bugs are listed below.

1.  -  *Issue*: If a user created the account and would just get general information, credentials would have not been saved in the external sheet.
    - *Solution*: Instead of saving all data directly in update_worksheet at the end of calculate dog, the developer adds update_worksheet when selecting end program so that also if the user created the account and ends the program, the user information will be saved.
2.  -  *Issue*: When saving and calculating two dogs, instead of showing in the table in different lines, all info was appended to the same line,     
    modifying all data and final tabulate.
    -  *Solution*: Developer searched for a way of clearing the global variables where saving the list of information, each time the user wanted to calculate a new dog.
    Used [StackOverflow](https://stackoverflow.com/questions/850795/different-ways-of-clearing-lists) : del INFO[:] 
    Empty the list before starting to calculate a new dog.
3.  -  *Issue*: When calculating mer the calculation would have always returned that the dog was underweight also if it shouldn't.
    -  *Solution*: Typing mistakes of the developer was using the wrong index from saved data that return wrong calculations. Change for the right index to fix minor issues.
4.  -  *Issue* : Big issue found when printing the tabulate in show_dogs function. When the user login it would have worked perfectly, while when creating the 
    account, it was displaying an empty tabulate.
    -  *Solution*: To find the solution the developer first prints out all the data to see if not correct data were arriving in the final function. When checked that all data were correct, the developer try to understand the difference in the path between login and creating an account. The only difference was the Unicode. But the Unicode was arriving in the final function perfectly when printed out in the final function Unicode was correct. At that point, the developer thought that the path for the Unicode to arrive was different. From login, it would have arrived from the external sheet, while creating the account from another function. So that is how the developer arrive at to understand that the *Type* of Unicode was different. Printing out the Unicode developer saw that one was an INT and the other a STR. To fix the error finally developer just implemented in last function str(Unicode).


## Technology Used

### Languages Used

The main language used was **Python**.
All other languages used were provided by **Code institute** to use as a base to show the deployed project.

### External Programs-Website Used


-The developer used different external programs throughout the development of this project.

Below are all the external programs used :
- [Heroku]()
     - Heroku was used to deploy a final project.
- [GitPod](https://gitpod.io/ "Link to GitPod homepage")
     - GitPod was used for writing code, committing, and then pushing to GitHub.
- [GitHub](https://github.com/ "Link to GitHub")
     - GitHub was used to store the project after pushing.
- [Canva](https://www.canva.com/ "Link to Canva homepage")
     - Canva was used to create structural and formulas maps.
- [Am I Responsive?](http://ami.responsivedesign.is/# "Link to Am I Responsive Homepage")
     - Am I Responsive was used to see responsive design throughout the process and to generate mockup imagery to be used.
- [Ezgif](https://ezgif.com/video-to-gif "Link to go to ezgif homepage")
    - Ezgif was used to convert all videos to gifs for the testing file.
- [Free screen recorder](https://screencast-o-matic.com/screen-recorder?from=app&installed=true "Link to go to Free screen recorder homepage")
    - Free screen recorder was used to screen record all videos for the testing files.


## Testing

Testing information can be found in a different Testing [file](TESTING.md "Link to testing file")

## Credits

### Content

All knowledge on which formulas to use for all calculation in the project, and all general information were token by the developer from the following:

#### General information

General information are displayed in get general information and were taken from the following articles:

- *Dangerous food for dogs* : [Pets](https://pets.webmd.com/dogs/ss/slideshow-foods-your-dog-should-never-eat "Link to pets specific article")
- *Human food good for dogs* : [Cosmicpet](https://www.cosmicpet.com/blogs/news/12-healthiest-human-foods-for-dogs "Link to Cosmicpet specific article") and [MarieClaire blog](https://www.marieclaire.it/lifestyle/coolmix/a19428033/cosa-dare-da-mangiare-al-cane/ "link to Marieclaire specific article")
- *Four healthy habits for dogs* : [Daisybeet](https://www.daisybeet.com/4-healthy-habits-to-establish-for-your-dog/#:~:text=Dogs%20thrive%20with%20a%20daily,expected%20of%20them%20and%20when "Link to Daisybeet specific article")
- *BCS = Body condition score* : [Petmd](https://www.petmd.com/dog/nutrition/how-find-your-dogs-body-condition-score "Link to Petmd specific article")
- *When a dog become a senior* : [Thehealthypets](https://www.thehealthypetclub.co.uk/when-will-my-dog-become-a-senior/ "Link to Thehealthypets specific article")
- *6 signs your dog is healthy* : [Petinsurance](https://www.petinsurance.com/healthzone/pet-health/health-conditions/6-signs-your-dog-is-healthy/ "Link to petinsurance specific article")
- *Why and when contact the vet* : [Vetmd](https://vetmed.tamu.edu/news/pet-talk/when-to-call-a-veterinarian/ "Link to Vetmd specific article")

#### Formulas

The following formulas were find by the developer in order to calcolate ideal weight, and which value to use based on life stage of the dog:







