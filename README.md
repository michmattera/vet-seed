# **Vet Seed**


![vet Seed Mockup Images](/assets/images/read-me-images/)

[View the live project here](https://michmattera.github.io/)
     

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

Ideal user demographic for this programs are:
- Veterinarians
- People with basic information on bcs to calcolate calories per day for their dog

### User goals

Developer divided user goals for the following categories:
1. New user
2. Old user


**New user** 

Main goal are the following:

- Understand straight away what this program can offer
- Be able to create an account
- Get general information on dogs
- Be able to calcolate if my dog is overweight, underweight or ideal weight
- Calcolate which one should be the ideal weight of my dog
- Calcolate haw many calories per day I should give my dog
- See the summary of the calcolation in  atable or in a file

**Old user** 

Main goal are the following:

- Be able to login without creating another account
- Calcolate another dog calories and ideal weight
- Be able to have a summary of all dogs already inserted
- Read general info again if forget something

[Back to top ⇧](#Vet-Seed)

## Development Planes

Project purpose:

To build a command-line application that allows users to manage a common dataset about a particular domain.

Vet application was chosen by the developer for the personal interest of the developer in dogs , and to try and create something useful for an every day task to address specific target audiance. 

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

Developer goals were the following:
- Create an application that could pass throught validators without error
- Address an every-day need and try to simplify human tasks using language learned
- Present the application in a clean and easy to understand manner
- Try to give even if simple good UX experience

#### User needs

User needs were the following:
- Calcolate if a dog is under, over or ideal weight
- Calcolate how many calories to give to dog based on the weight
- Have visual effect if wrong or right input inserted
- Summary at the end of the program with all information displayed
- Few questions to simplify process
- After each section choice to end program

The developer has to get following information about the user:
- Username
- Password
- Unicode ( just for login )


 When username and password are created and validated ,a random number called *Unicode* will be assigned to user.

User will have to save this number in order to login.


The developer has to get following information about the dog:
- Name
- Weight
- BCS (Body Score condition)
- Life Stage


### Scope

Now that we have established the goals of the program we can deduce the necessary features:

1. Multiple choice for user to let him decide what he would actually like to do
2. Inputs to insert required data
3. Color effect on wright and wrong values inserted
4. Message user frequently based on the process and the values given
5. Calcolate final calories per day to give dog
6. Calcolate difference of weight an ideal weight
7. Table to insert at the end of program for summary of values provided and calculated
8. Saved user data in external sheet
9. Save dogs data to be able to access it when user login

### Structure

Structure for the application was made using [Canva](https://www.canva.com/ "Link to Canva").

Firstly the developer searched all information online to see how to calcolate everything and create basic structure.

With the information found then she created formulas chart.

<details>
<summary>Formulas for flowchart</summary>
    
![Formulas](assets/images/scheme-formulas.png)

</details> 

Then the developer create a structural map based on importance and on how to calcolate everything.


The structure was then divide in two main sections:
1. General info = Where the user will just get information
2. Main section = Where the user will insert data and get back result

<details>
<summary>Map structure</summary>
    
![Map structure](assets/images/structure-map.png)

</details> 

Map structure was change slightly , adding in multiple choice possibility to user to show saved dogs in tabulate.

[Back to top ⇧](#Vet-Seed)


## Features

### General features

- **General section** = User will get general information and advices on dogs based on  weight, bcs, and life stage.
- **Input**:
    1. **Name** = Name of dog ( max 10 letters )
    2. **Weight** = Weight of the dog measured in the moment ( from 0 to 100 kg)
    3. **BCS** = 0 to 9 ( 9 scale bcs )
    4. **Life Stage** = Depending on the following criterias:
        - Working dog = Exercise( Light: 2 - Moderate: 4 - Heavy: 6)
        - No working dog = If dog ( Intact: 1.8 - Neutered: 1.6)
        - Ideal, over or under weight = If dog ( Ideal weight: lifeStage * weight - Over/Under weight: lifeStage * ideal weight)
- **Calcolation**:
    1. **Ideal weight** = Based on bcs and weight
    2. **Calories** = How many calories per day should the dog get based on ideal weight and life stage.
- **Save data** = All data inserted from user were then saved in external google sheet.
- **Table** = Summary table at the end of application with all data inserted from user and conclusion.
- **Multiple choice** = Used mainly to change section from main to general and vice versa . Or to restart and end program.
- **Visual effect** = To give user better UX experience.

### Future features

Due to limited resources (time constraints, skills of the developer at the moment, and other reasons), some features were not implemented.

1. Be able to access old dogs datas with login and be able to updated already saved datas with new values. Having updated datas showed as well in final summary.

## Design

The design of a command line application is usually very simple. The developer though decided that for a better UX experience would be implemented:
- **Colors**:
    1. **Red** = Would be assign to a wrong value inserted by the user to help him visualize the error.
    2. **Green** = Would be assign to correct value inserted by user to help him visualize no error was given, when datas are saved correctly and intrto and ASCII art.
    3. **Blue** = Would be assign to general information and return calcolation to highlight it from other text.
    4. **Yellow** = Would be assign to datas that indicate important datas, such as if dog is underweight or overweight.
- **Space** = More space between sections and important sentences to highlight right information.
- **Time** = Between different functions and calcolation for better UX.
- **Clear** = Functionality to eliminate section by section to not overwhelm the user with information.
- **Intro design** = Intro design using ASCII art, to give better user experience.
- **Tabulate** = Fancy tabulate in blue, to give better user experience when showing saved information to user.

## Issues and bugs

The developer found different issues and bugs during the creation of the application , main issues and bugs are listed below.

1.  -  *Issue* : If user created the account and would just get general information, credentials would have not saved in external sheet.
    - *Solution* : Instead of saving all datas directly in update_worksheet at the end of calcolate dog, developer add update_worksheet when selected end program so that also if the user created the account and end the program , the user information will be saved.
2.  -  *Issue* : When saving and calcolating two dogs, instead of showing in the table in to different lines, all info were appended to the same line ,     
    modifying all datas and final tabulate.
    -  *Solution* : Developer searched for a way of clearing the global variables where saving the list of information, each time the user wanted to calcolate new dog.
    Used [StackOverflow](https://stackoverflow.com/questions/850795/different-ways-of-clearing-lists) : del INFO[:] 
    Empty the list before starting to calcolate new dog.
3.  -  *Issue* : When calcolating mer the calcolation would have always return that dog was underweight also if it shoudn't.
    -  *Solution* : Typing mistaked of developer wa susing wrong index from saved datas that return wrong calcolations. Change for right index to fix minor issue.
4.  -  *Issue* : Big issue found when printing the tabulate in show_dogs function. When user login it would have worked perfectly, while when creating the 
    account , it was displaying an empty tabulate.
    -  *Solution* : To find the solution the developer firstly print out all the datas to see if not correct datas were arriving in final function. When checked that all datas were correct , the developer try to understand the difference of path between login and create account. The only difference was the Unicode . But the unicode was arriving in final function perfectly when printed out in final function unicode was correct. At that point developer thought that the path for the unicode to arrive was different. From login it would have arrived from the external sheet, while creating the account from another function . So that is how developer arrive to understand that the *Type* of unicode was different. Printing out the unicode developer saw that one was an INT and the other a STR. To fix the error finally developer just implemented in last function str(Unicode).


## Technology Used

### Languages Used

Main language used was **Python**.
All other languages used were provided from **Code institute** to use as base to show deployed project.

### External Programs-Website Used


-The developer used different external programs throughout the development of this project.

Below are all external programs used :
- [Heroku]()
     - Heroku was used to deploy final project.
- [GitPod](https://gitpod.io/ "Link to GitPod homepage")
     - GitPod was used for writing code, committing, and then pushing to GitHub.
- [GitHub](https://github.com/ "Link to GitHub")
     - GitHub was used to store the project after pushing.
- [Canva](https://www.canva.com/ "Link to Canva homepage")
     - Canva was used to create structural and formulas map.
- [Am I Responsive?](http://ami.responsivedesign.is/# "Link to Am I Responsive Homepage")
     - Am I Responsive was used to see responsive design throughout the process and to generate mockup imagery to be used.
- [Ezgif](https://ezgif.com/video-to-gif "Link to go to ezgif homepage")
    - Ezgif was used to convert all videos to gifs for the testing file.
- [Free screen recorder](https://screencast-o-matic.com/screen-recorder?from=app&installed=true "Link to go to Free screen recorder homepage")
    - Free screen recorder was used to screen record all videos for the testing files.






