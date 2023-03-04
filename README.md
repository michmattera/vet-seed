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
This is a back-end program to facilitate the job of veterinarians to calcolate and save data of subjects (in this case dogs) , calcolate if the dog is underweight, overweight or in ideal weight, in addition calcolate as well calories per day that dog should take based on weight and life stage.

The developer wanted to address a real-every-day problem or calcolation to facilitate and save data's just by answering a few questions.

This is a program created for the third of five Milestone projects required to complete the Diploma in Software development (eCommerce Applications) program at The Code Institute.
The main requirement of this project is to use  **PYTHON** as the main technology. 

## **UX**

### Ideal User demographic

Ideal user demographic for this programs are:
- Veterinarians
- People with basic info on bcs to calcolate calories per day for their dog

### User goals

Developer divided user goals for the following categories:
1. New user
2. Old user


**New user** main goal are the following:

- Understand straight away what this program can offer
- Get general information on dogs
- Be able to calcolate if my dog is overweight, underweight or ideal weight
- Calcolate which one should be the ideal weight of my dog
- Calcolate haw many calories per day I should give my dog
- See the result in a table or in a file

**Old user** main goal are the following:

- Calcolate another dog calories and ideal weight
- Update existing information of dog with new weight and progress
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

Chosen target audience: veterinarian - people with basic vet information

#### Developer Goals

Developer goals were the following:
- Create an application that could pass throught validators without error
- Address an every-day need and try to simplify using language learned
- Present the application in a clean and easy to understand manner
- Try to give even if simple good UX experience

#### User needs

User needs were the following:
- Calcolate if a dog is under, over or ideal weight
- Calcolate how many calories to give to dog based on the weight
- Have visual effect if wrong or right input inserted
- Summary at the end of the program with all information displayed
- Few questions and answer to simplify process
- After each section choice to end program or restart

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
5. Calcolate calories per day
6. Calcolate difference of weight an ideal weight
7. Table to insert at the end of program for summary of values provided and calculated
8. Saved data in external sheet

### Structure

Structure for the application was made using [Canva](https://www.canva.com/ "Link to Canva").

Firstly developer searched all information online to see how to calcolate everything and create basic structure.

<details>
<summary>Formulas for flowchart</summary>
    
![Formulas](assets/images/scheme-formulas.png)

</details> 

Then the developer create a structural map based on importance and on how to calcolate everything.


The structure was then divide in two main sections:
1. General info = Where the user will just get information
2. Main section = Where the user will insert data and gety back result

<details>
<summary>Map structure</summary>
    
![Map structure](assets/images/structure-map.png)

</details> 

[Back to top ⇧](#Vet-Seed)


## Features

### General features

- **General section** = User will get general information and advices on dogs based on age, size, weight.
- **Input**:
    1. **Name** = Name of dog ( max 10 letters )
    2. **Weight** = Weight of the dog measured in the moment ( from 0 to 100 kg)
    3. **BCS** = 0 to 9 ( 9 scale bcs )
    4. **Life Stage** = Depending on the following criterias:
        - Working dog = Exercise( Easy: 2 - Medium: 4 - Heavy: 6)
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

.............................................

## Design

The design of a command line application is usually very simple. The developer though decided that for a better UX experience would be implemented:
- **colors**:
    1. **Red** = Would be assign to a wrong value inserted by the user to help him visualize the error.
    2. **Green** = Would be assign to correct value inserted by user to help him visualize no error was given.
    3. **Blue** = Would be assign to important datas and return calcolation to highlight it from other text.
- **Space** = More space between sections and important sentences to highlight right information.
- **Time** = Between sentences and calcolation for better UX.
- **Clear** = Functionality to eliminate section by section to not overwhelm the user with information.
- **Intro design** = ................................................................






