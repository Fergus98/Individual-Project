# Individual-Project


# Introduction

This project looks at the steps taken and the completion of a baseball scoring system. I am a big fan of baseball and thought it would be fun to create a way of amateur teams keeping a leaderboard similar to MLB (Major League Baseball). The system will allow users to create their teams and games. From there they can add the names etc. of the players who are in the team and playing the game. The application will store the team’s games and users will be able to look at the season’s scores and players scores also. 

# User Stories

As a user I want to be able to add teams so we can track our progress.
As a user I want to be able to add players so I can have my team members tracked.
As a user I want to be able to add scores for the teams so I can track our progress.
As a user I want to be able to add runs so I can keep score.
As a user I want to be able to add games so I can keep track of multiple games.

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

I decided to create some rough wireframes to visualise the design of the application. This allowed me to break down the pages that I would need to create in order to get the CRUD functional application.








# CI Pipeline

![CI Pipeline](https://user-images.githubusercontent.com/9552989/76163766-f38b1100-6140-11ea-97b1-6c49be7e4151.jpg)



# Test Cases

Test Case No.
Input
Output
#1
get(url_for('showGames'))
assertEqual(response.status_code, 200)
#2
get(url_for('showTeams'))
assertEqual(response.status_code, 200)
#3
get(url_for('showPlayers'))
assertEqual(response.status_code, 200)
#4
get(url_for('createGame'))
assertEqual(response.status_code, 200)
#5
get(url_for('createTeam'))
assertEqual(response.status_code, 200)
#6
get(url_for('createPlayer'))
assertEqual(response.status_code, 200)
