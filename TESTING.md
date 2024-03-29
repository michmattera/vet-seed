# **VET-SEED - Testing** 

[Read Me file](/README.md)

[View Github repository](https://github.com/michmattera/vet-seed)

[View the live project here](https://vet-seed.herokuapp.com/)


## **Table of contents**
***
1. [Manual Testing](#manual-Testing)
    1. [User Inputs](#user-inputs)
        - [Incorrect Inputs](#incorrect-inputs)
        - [Correct Inputs](#correct-inputs)
    2. [Getting datas](#getting-datas)
        - [Introduction](#introduction)
        - [General information](#general-information)
        - [Show saved dogs](#show-saved-dogs)
2. [Code validation](#code-validation)
3. [Bugs](#bugs)

## Manual testing

Manual testing was performed after deploying the project to heroku platform.

### User Inputs


#### Incorrect Inputs

Incorrect inputs were tested with the following criterias:

| Input | Empty | Lenght | Type | All |
| --- | --- | --- | --- | --- |
|  Login - Create | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: |
| Login | - | - | - | :heavy_check_mark: |
| Create Username | :heavy_check_mark: | :heavy_check_mark: | - | :heavy_check_mark: |
| Create Password | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: |
| Confirm Change | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: |
| Ready | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: |
| General info | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: |
|  Calcolate Calories name | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: |
|  Calcolate Calories weight | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: |
|  Calcolate Calories bcs | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: |
|  Is work dog | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: |
|  Type exercise | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: |
|  Neutered Intact | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: |
| Multiple choice | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: |

All incorrect error were checked after deployment , and all bugs or issue were then handled by the developer, making small chganges.

The following files shows all **incorrect input** of the user in the specific section:



<details>
<summary> Login - Create</summary>

![Error Login - Create](assets/images/testing-files/errors-login-create.gif)

</details>

<details>
<summary> Login</summary>

![Error login](assets/images/testing-files/error-login.gif)

</details>

<details>
<summary> Create username</summary>

![Error username](assets/images/testing-files/error-username.gif)

</details>

<details>
<summary> Create password</summary>

![Error password](assets/images/testing-files/error-password.gif)

</details>

<details>
<summary> Confirm change</summary>

![Error password](assets/images/testing-files/error-confirm-change.gif)

</details>

<details>
<summary> Ready</summary>

![Error password](assets/images/testing-files/error-ready.gif)

</details>

<details>
<summary> General information</summary>

![General information](assets/images/testing-files/error-general-info.gif)

</details>

<details>
<summary> Calcolate calories error name</summary>

![Error calc-calories name](assets/images/testing-files/error-calc-calories-name.gif)

</details>

<details>
<summary> Calcolate calories error weight</summary>

![Error calc-calories weight](assets/images/testing-files/error-calc-calories-weight.gif)

</details>

<details>
<summary> Calcolate calories error bcs</summary>

![Error calc-calories bcs](assets/images/testing-files/error-calc-calories-bcs.gif)

</details>

<details>
<summary> Is work dog</summary>

![Error is work dog](assets/images/testing-files/error-work-dog.gif)

</details>

<details>
<summary> Type of exercise</summary>

![Error type of exercise](assets/images/testing-files/error-type-exercise.gif)

</details>

<details>
<summary> Neutered intact</summary>

![Error neutered intact](assets/images/testing-files/error-neutered-intact.gif)

</details>

<details>
<summary> Multiple choice</summary>

![Error multiple choice](assets/images/testing-files/error-multiple-choice.gif)

</details>


#### Correct Inputs


All correct inputs should display a message to user for better UX.
Correct inputs were all tested and checked.


| Input | Checked |
| --- | --- |
| Login - end program| :heavy_check_mark: |
| Create account | :heavy_check_mark: |
| Overweight|  :heavy_check_mark: |
| Ideal weight | :heavy_check_mark: |
| Underweight | :heavy_check_mark:|



<details>
<summary> Login - End program</summary>

![Login - End program](assets/images/testing-files/correct-login-end-program.gif)

</details>

<details>
<summary> Create account</summary>

![Create account](assets/images/testing-files/create-account.gif)

</details>

<details>
<summary> Overweight</summary>

![Overweight](assets/images/testing-files/overweight.gif)

</details>

<details>
<summary> Ideal weight</summary>

![Ideal weight](assets/images/testing-files/ideal-weight.gif)

</details>

<details>
<summary> Underweight</summary>

![Underweight](assets/images/testing-files/underweight.gif)

</details>

### Getting datas


All general information are generated thanks to gspread, with an external sheet created by the developer.
All general information were tested to check they were displayed following the time , the space and to check that the right information were taken from the external sheet.

#### Introduction

<details>
<summary> Introduction</summary>

![Introduction](assets/images/testing-files/intro.gif)

</details>



#### General information

| General information | Checked |
| --- | --- |
| Dangerous food for dogs | :heavy_check_mark: |
| Human food good for dogs | :heavy_check_mark: |
| Four healthy habits for dogs |  :heavy_check_mark: |
| Bcs | :heavy_check_mark: |
| When a dog became a senior | :heavy_check_mark:|
| 6 Signs Your Dog is Healthy | :heavy_check_mark:|
| Why and when contact vet | :heavy_check_mark:|

<details>
<summary> Dangerous food for dogs </summary>

![Dangerous food for dogs](assets/images/testing-files/gen-info-one.gif)

</details>

<details>
<summary> Human food good for dogs </summary>

![Human food good for dogs](assets/images/testing-files/gen-info-three.gif)

</details>

<details>
<summary> Four healthy habits for dogs </summary>

![Four healthy habits for dogs](assets/images/testing-files/gen-info-four.gif)

</details>

<details>
<summary> Bcs </summary>

![Bcs](assets/images/testing-files/gen-info-two.gif)

</details>

<details>
<summary> When a dog became a senior </summary>

![When a dog became a senior](assets/images/testing-files/gen-info-five.gif)

</details>

<details>
<summary> 6 Signs Your Dog is Healthy </summary>

![6 Signs Your Dog is Healthy ](assets/images/testing-files/gen-info-six.gif)

</details>

<details>
<summary>Why and when contact vet </summary>

![Why and when contact vet](assets/images/testing-files/gen-info-seven.gif)

</details>



#### Show saved dogs

To check that the information inserted from the user, and then displayed the developer show that in the account logged no dogs were saved , than calculated one and then display dogs again to show that all the information saves correctly.
In the meanwhile all correct input to calcolate dog are shown as well.

<details>
<summary>Show saved dogs</summary>

![Show saved dogs](assets/images/testing-files/show-dogs.gif)

</details>


### Code validation 

To validate the code the developer used the following program Pyhton [linter](https://pep8ci.herokuapp.com/ "Link for python linter") provided by code institute , where no errors were found.

<details>
<summary>Python linter</summary>

![Python linter](assets/images/testing-files/python-linter.gif)

</details>


### Bugs

Following bug was found by the developer but for limited time , could not be able to fix it.

Each time the user press enter the text goes 
The bug occurs when a keyboard press from user during slow_type.

- Each time he presses enter the text wraps.
- Each time he press a letter or number it is pressed into the text.
- Each time he presses something,  when the text ends , an error is given as if he had pressed when an option is presented and failing to give one of the correct options he is presented with the specific error. As it should happen when user insert incorrect input.


Developer tried to fix the bug trying the following:

-  installed getch
- tried to inport keyboard and msvcr but with no positive result

Ending with the bug unsolved.

Following file on unsolved bug:

<details>
<summary>Bug</summary>

![Bug](assets/images/testing-files/known-bug-keyboard.gif)

</details>










