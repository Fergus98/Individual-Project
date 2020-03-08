# Individual-Project


# Introduction

This project looks at the steps taken and the completion of a baseball scoring system. I am a big fan of baseball and thought it would be fun to create a way of amateur teams keeping a leaderboard similar to MLB (Major League Baseball). The system will allow users to create their teams and games. From there they can add the names etc. of the players who are in the team and playing the game. The application will store the team’s games and users will be able to look at the season’s scores and players scores also. 

# User Stories

- As a user I want to be able to add teams so we can track our progress.
- As a user I want to be able to add players so I can have my team members tracked.
- As a user I want to be able to add scores for the teams so I can track our progress.
- As a user I want to be able to add runs so I can keep score.
- As a user I want to be able to add games so I can keep track of multiple games.

# Entity Relationship Diagram

The entity relationship diagrams I created provided the relationships for the database I will create for the application. 

# Requirements

Functional
Non-functional
Create Games
Easy to navigate website
Create Players
Nice to use
Create Teams


Update Games







# Risk Assessment

My risk assessment attempts to cover all potential risk that could occur during the project, and any measures I can take to prevent aforementioned risks.

Risk
Likelihood
Impact
Action
Illness
Medium
Medium, would slow work 


Running out of time
Low
High, product would be unfinished
Work on MVP, ensure MVP is completed
Losing Code
Medium
Medium, progressed slowed
Using GitHub, saved off laptop

















# Trello Board

https://trello.com/b/CG5JGmIm/personal-project-sprint-1

# Wireframes 

I decided to create some rough wireframes to visualise the design of the application. This allowed me to break down the pages that I would need to create in order to get the CRUD functional application. The pages for Create Team, Create Player, show Team and Show Player, would be almost exactly the same as the Create and Show Games pages.


<img width="401" alt="HOMEWIREFRAME" src="https://user-images.githubusercontent.com/9552989/76164127-3c909480-6144-11ea-9869-223452c85576.PNG">

<img width="400" alt="CREATEGAMEWIREFRAME" src="https://user-images.githubusercontent.com/9552989/76164130-431f0c00-6144-11ea-8db6-77900e19d6cd.PNG">

<img width="399" alt="SHOWGAMESWIREFRAME" src="https://user-images.githubusercontent.com/9552989/76164134-474b2980-6144-11ea-9286-0d8aa175e4c0.PNG">


# CI Pipeline

Below is an image of the CI pipeline that my project follows. The Jenkins VM will automatically pull code from GitHub once it detects a new change/commit. It will then run the tests locally in the Jenkins VM, if the tests are successful, the app will automatically build and deploy to a seperate VM. Jenkins also sets up the connection for the seperate database instance hosted on azure.

![CI Pipeline](https://user-images.githubusercontent.com/9552989/76163766-f38b1100-6140-11ea-97b1-6c49be7e4151.jpg)



# Test Cases

Below are the test cases created to test the system.

<img width="378" alt="TESTCASES" src="https://user-images.githubusercontent.com/9552989/76163792-26350980-6141-11ea-8483-28038e5b5a55.PNG">

