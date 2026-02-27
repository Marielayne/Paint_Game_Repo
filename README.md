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
- The GUI code should be modular to allow readability and and more efficient processing. 

**4.	Portability:**
- The GUI should work on both Mac IOS and Windows IOS,
- The system should rely on standard Python libraries (including Tkinter, csv, os, random and re) for ease of use for future developers and to encourage longevity.

#### GUI Framework with Figma
![Alt Text](https://github.com/Marielayne/Paint_Game_Repo/blob/main/1.png)
![Alt Text](https://github.com/Marielayne/Paint_Game_Repo/blob/main/2.png)
![Alt Text](https://github.com/Marielayne/Paint_Game_Repo/blob/main/3.png)
![Alt Text](https://github.com/Marielayne/Paint_Game_Repo/blob/main/4.png)


#### Class Diagram with draw.io
![Alt Text](https://github.com/Marielayne/Paint_Game_Repo/blob/main/C.D..png)

### References
 [Image 1: AkzoNobel - Sikkens coating for McLaren F1 car](https://www.ipcm.it/en/post/akzonobel-powers-mclarens-2025-f1.aspx)
