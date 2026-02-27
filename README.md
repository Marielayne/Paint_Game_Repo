# Paint_Game_Repo
## My Summative Assessment Two Submission
### Introduction 
At AkzoNobel we manufacture paints and coatings for a wide range of industries and customers. Such examples include manufacturing coatings for ships which need to be durable against marine life and conditions, coatings for aeroplanes, paints and primers for vehicles including specialised vehicles such as McLarens Formula 1 car, interior and exterior wall paints that have different purposes and functionality. As a result of the high demand industries that we work in, a deep knowledge and understanding of how paint is formulated is required. We strive to provide the best performance to provide us with an edge over competitors which reducing the environmental impact. 

The department in which we work focuses on interior wall paint primarily used for customers to use on home projects or for small businesses such as decorators. To do this we experiment with the formulations to improve test results or environmental impact. This GUI is a simple way to test new employees understanding of our tests and performance indicators. For instance, the quiz will ask basic questions such as “what is opacity”. The assumption is the new starts would have been trained on this prior and thus, should know the correct answers (multiple choice). However, for those who have not been trained or need support, the answers are available online. The GUI saves the data to a csv file and takes the names of participants. This provides employers with evidence of understanding from the training and peace of mind to allow them to begin creating and testing paint formulations. For the sake of this repo, questions have been kept minimal and general to prevent leaking trade secrets.

![Alt Text](https://www.ipcm.it/upload/img/c/600x400-AkzoNobelPowersMcLarens2025F1SeasonwithAdvancedCoatingsTechnology.jpg)

### Design
#### A brief overview: 
This app aims to take teams of 1 – 10 players and save their responses to 8 questions regarding paint testing. The data will be saved in a csv file as it simple, transferable to multiple systems and low on storage and processing power. The game should run smoothly, with no error causing the game to break and the data to be incomplete. There will be validations in place to ensure that valid data is entered into the csv data set. The questions will be multiple choice to make counting the players score easier and to reduce the amount of code needed to run the game. This will make processing the GUI faster, make TDD easier and more efficient. Multiple choice questions are sufficient for the purpose of the game; to ensure understanding of the new starters at the company. 
The images below show the frame work design used to guide the GUI build process and the Class Diagram used to organise the data stored for csv. 



#### Functional Requirements:
**1.	Team Setup:**
- The team need to be able to enter their team name before starting the quiz,
-	The department will need to be selected from a pre-defined list to prevent incorrect selection. This ensures easy filtering and processing of data later when it comes to analysing,
- The team can choose the size of the team (1-10) and enter the player names as required,
- The code must then save the data entered by the team for use during the quiz. 

**2.	Input Validation:**
- The GUI should prevent the game from starting if no team name is entered,
- The member names should be reasonable with no numbers or special characters except for a hyphen to allow double-barrelled names,
- The GUI should ignore blank player fields as players may not realise the impact that could have on the code and thus, the data stored,
- The GUI will not allow players to skip a question. 

**3.	Quiz functionality:**
- The quiz will display one question at a time,
- The quiz will be multiple questions,
- The user should be able to submit an answer for each question,
- The GUI should check that answer against the correct selection,
- The GUI will store that answer to count towards a score that will be provided at the end of the quiz,
- The GUI will send a message box indicating if the users got the question correct,
- The GUI will calculate the percentage of their scores and reflect this on the end screen,
- The quiz will allow the users to repeat the quiz.

**4.	Data Storage:**
- The GUI will save the data to a csv file and allow multiple teams to submit to the same csv,
- The system shall create the csv if it does not already exist,
- The storage data shall include “Team name” “Department”, “Team Members”, “Score”, “Percentage”,
- All the team members will be stored in one column to negate the effects of multiple players changing the number of columns required for the csv. Names will be stored as string.

#### Non-Functional Requirements:
**1.	Usability:**
- The GUI should be clear and easy to read allowing all to be able to use the interface regardless of skill or learning difficulty,
- The GUI should have clear instructions,
- Layout should remain consistent throughout.
  
**2.	Performance:**
- The GUI should run smoothly with no noticeable delay,
- The GUI should handle up to 10 participants without performance restrictions,
- The GUI shall not crash and break out of code due to error,
- The data should be saved safely to avoid loss of previous results. 

**3.	Maintainability:**
- The GUI should use classes for efficient storage and calling of functions and attributes and to allow future expansion,
- Quiz data shall be stored externally to allow easy future updates without interaction with main GUI code,
- The GUI code should be modular to allow readability and more efficient processing. 

**4.	Portability:**
- The GUI should work on both Mac OS and Windows OS,
- The system should rely on standard Python libraries (including Tkinter, csv, os, random and re) for ease of use for future developers and to encourage longevity.

#### GUI Framework with Figma
![Alt Text](https://github.com/Marielayne/Paint_Game_Repo/blob/main/1.png)
![Alt Text](https://github.com/Marielayne/Paint_Game_Repo/blob/main/2.png)
![Alt Text](https://github.com/Marielayne/Paint_Game_Repo/blob/main/3.png)
![Alt Text](https://github.com/Marielayne/Paint_Game_Repo/blob/main/4.png)

#### Class Diagram with draw.io
![Alt Text](https://github.com/Marielayne/Paint_Game_Repo/blob/main/C.D..png)

### Development 
Line 1 – 7

This section of code imports relevant modules and libraries to allow the code to work. Tkinter is the library used to generate the GUI window and pin the user input elements to the window. It allows you to select the type of input fields, the location of those fields, the colour of the fields, text and the background and more. It is all related to creating the Graphical User Interface. Random is a library that allows the generation of random data which you can either predefine or allow Python to select from its pre-existing library. This GUI uses it to randomise the responses for the user after entering an answer. csv allows for the developer to read and write data into a csv. This GUI uses it to get data from the input fields and append a csv to create a dataset. os is used to ensure the csv can be saved to Mac or Windows as their operating systems work differently. 

Lines 9 – 33

This section defines the classes, its attributes and the functions. It is an example of object-oriented programming (OOP). Doing this allowed me to structure objects instead of using lots of separate variables. The aim was to keep the main GUI file clear and easy to read for future developers to take over or make amends. The question data stored in the child class is stored in another file to maintain readability and allow for changes to be made without risking any code in the main GUI. This is because any changes to questions or answers are stored in another file. The classes just call upon these variables stored in dictionaries and tuples in another file. 

The parent class team stores the basic information regarding the team that is collected on the first page. From there the child class inherits this team data e.g. the team name and members and then stores the quiz answers and running total in relation the data acquired from the parent class. “def __init__” counts the scores while “def get_csv_data” frames the csv file and how all the data will be presented in csv format. 

Line 35 – 192

This section of code generally focusses on setting up the GUI. For instance, there is a lot of code regarding formatting of input fields. Such examples include lines **75 – 80**. This part of the code shows the code that decides how the name input fields would look and provides the geographical code for where the input field should be rooted. Row **85 – 116** is a bit more complicated as the aim was to increase the number of fields or decrease them depending on the number of team members. 

line 85 - 116

The code for the dynamic team members fields is broken down in to digestible chunks; Department dropdown, member count and dynamic fields and update members fields. Department dropdown places the widget to the GUI, providing the departments than can be selected in a list. The selected input is then stored as a string. The members count and dynamic field section places the widget by creating the frame, it then stores the number of members in the variable “members_count” and automatically updates when the user changes the value in the spinbox. The default value is 1. The code then counts the values in the spinbox and defines a limit of 1 – 10 can be created and destroyed. Every time a user increases or reduces the value in the spinbox, the number of member fields will change as the code updates the member’s field. This is because “updates_members_fields()” updates automatically. 

Line 118 to 137

This portion of the code shows a function which allows the quiz to function as a quiz. It calls upon global variables which allows the code to be used across different functions within the app. Without this, Python would treat them as local variables and other functions such as “show_question()” wouldn’t see the updated values. This then appears multiple times throughout the remainder of the code. 
This code uses .get().strip() which is a simple validation process to remove accidental spaces. This helps to clean the data and it is then stored in a new variable called “team_name_val”. 
The code then gets the data such as selected department, member names, (which have been stripped) and stores the data in preparation for the start of the quiz. 

Line 138 – 187

This section of code is dedicated to defining functions that show the questions, check the answers and finally show the results. It calls upon the global variables again to track which question the user is on, and then ends the quiz once “if question_index >= len(questions)” has counted through all the questions stored in the questions variables in the question file. It then prints the stored and calculated result to the user so they can see their score or continues to cycle through the questions. 

### Testing
 Automated testing was used with unittesting. This method was selected as it makes the most sense to me out of the options I have tried. The use of unittest is beneficial as it improves code quality. It does so by providing a “safety net” as it forces the developer to think of errors that will occur ahead of time. This causes the developer to think of the errors ahead of time while writing the code which reduces the error in the code in the first place. 
 
Secondly, unit testing before the code is even written with clear “fail” or “ok” feedback helps track errors as they occur. This makes for easier development as errors can be dealt with straight away instead of tracking them down later and potentially changing the entire code to fix the errors. 
These two examples alone lead to reduced debugging time so makes the development process more efficient. It also leads to modularity and thus better design of the main code as it encourages the developer to write smaller testable units of code. 

I favoured this method of manual testing which involves running the programme each time a section of code is added. While I did do this to an extent (as I had additional ideas of things to add as the project developed), It proved timely as I had to run through the entire quiz each time. Something I’ve learned from this experience is to plan out the unit test as I did the quiz framework. I had a general idea of things I knew I wanted to test but it would have been more effective to have planned it ahead of time along side the GUI framework. Reason for this is to avoid having to do any manual testing because I hadn’t already written the unittest.  

My tests did pass however, I do not have enough tests to cover all the functions within my GUI. This is due to lack of forward thinking while writing the unit test and using manual tests to replace this. 
Such example includes the validation of the member names. I tried to include a regex code to prevent unreasonable entries, however, I forgot to include this ahead of time and once the code was written, it was too hard to fix. Hence, the importance of planning the TDD better ahead of time. 

### Documentation
#### User Documentation

**Enter Team Details**
- Team Name (required)
- Department (select from dropdown: R&D, Sales, Supply chain, Retail, Customer service)
- Team Size (1–10)
- Enter each team member’s name in the dynamically generated fields

**Start the quiz**
- Click the button "Start Quiz" to progress to the next screen

**Answer Questions**
- Select one option per question
- Click Submit Answer
- Popups show if the answer is correct or incorrect
- Select okay and move on to the next question

**View Results**
- Final score and percentage are displayed
- Options: Restart or Quit

**CSV Storage**
- Results are automatically saved to quiz_results.csv in the project folder
- Includes: Team Name, Department, Member Names, Score, Percentage

**Features**
- Dynamic team member input based on team size
- Multiple-choice questions with instant feedback
- Tracks score and calculates percentage
- Saves results to CSV
- Single-window GUI with restart/quit options
  
#### Technical Documentation
**Requirements**

- Python 3.8 or higher – The code uses modern Python syntax and modules [Download Python from here and select your operating system](https://www.python.org/downloads/)
- Tkinter module – Used for the GUI. Usually included with standard Python installations
- CSV module – Standard Python library, no extra installation required
- OS – Compatible with Windows, macOS, and Linux

### Evaluation

### References
 [Image 1: AkzoNobel - Sikkens coating for McLaren F1 car](https://www.ipcm.it/en/post/akzonobel-powers-mclarens-2025-f1.aspx)
 [Benefits of unittesting](https://medium.com/@anandvlinkedin/test-driven-development-the-unit-testing-advantage-e2f64024de29)
 
