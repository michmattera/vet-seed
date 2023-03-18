# **VET-SEED - Testing** 

[Read Me file](/README.md)

[View Github repository](https://github.com/michmattera/vet-seed)

[View the live project here]()


## **Table of contents**
***
1. [Manual Testing](#manual-Testing)
    1. [User Inputs](#user-inputs)
        - [Incorrect Inputs](#incorrect-inputs)
        - [Correct Inputs](#correct-inputs)
    2. [General information](#general-information)
    3. [Getting datas](#getting-datas)
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

![Login - End program](assets/images/testing-files/)

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

### General information

All general information are generated thanks to gspread, with an external sheet created by the developer.
All general information were tested to check they were displayed following the time , the space and to check that the right information were taken from the external sheet.

| General information | Checked |
| --- | --- |
| Login - end program| :heavy_check_mark: |
| Create account | :heavy_check_mark: |
| Overweight|  :heavy_check_mark: |
| Ideal weight | :heavy_check_mark: |
| Underweight | :heavy_check_mark:|

