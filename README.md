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

![Project 1 ERD](https://user-images.githubusercontent.com/9552989/76192941-de62c080-61da-11ea-875d-dc05a15b54bb.jpg)

# Risk Assessment

My risk assessment attempts to cover all potential risk that could occur during the project, and any measures I can take to prevent aforementioned risks.

<img width="380" alt="riskassessment" src="https://user-images.githubusercontent.com/9552989/76169081-dec47280-616c-11ea-9d12-047b62ec1dc2.PNG">



# Trello Board

https://trello.com/b/CG5JGmIm/personal-project-sprint-1

# Wireframes 

I decided to create some rough wireframes to visualise the design of the application. This allowed me to break down the pages that I would need to create in order to get the CRUD functional application. The pages for Create Team, Create Player, show Team and Show Player, would be almost exactly the same as the Create and Show Games pages.


<img width="401" alt="HOMEWIREFRAME" src="https://user-images.githubusercontent.com/9552989/76164127-3c909480-6144-11ea-9869-223452c85576.PNG">

<img width="400" alt="CREATEGAMEWIREFRAME" src="https://user-images.githubusercontent.com/9552989/76164130-431f0c00-6144-11ea-8db6-77900e19d6cd.PNG">

<img width="399" alt="SHOWGAMESWIREFRAME" src="https://user-images.githubusercontent.com/9552989/76164134-474b2980-6144-11ea-9286-0d8aa175e4c0.PNG">


# CI Pipeline

Below is an image of the CI pipeline that my project follows. The Jenkins VM will automatically pull code from GitHub once it detects a new change/commit. It will then run the tests locally in the Jenkins VM, if the tests are successful, the app will automatically build and deploy to a seperate VM. It will also notify slack of a successful or unsuccessful build. Jenkins also sets up the connection for the seperate database instance hosted on azure. 

![CI Pipeline (1)](https://user-images.githubusercontent.com/9552989/76166215-d3654d00-6154-11ea-8901-9321c35f33c7.jpg)



# Test Cases

Below are the test cases created to test the system. I managed to accomplish a 67% coverage.

----------- coverage: platform linux, python 3.6.9-final-0 -----------
Name                      Stmts   Miss  Cover
---------------------------------------------
application/__init__.py       9      0   100%
application/forms.py         25      0   100%
application/models.py        20      3    85%
application/routes.py        77     40    48%
---------------------------------------------
TOTAL                       131     43    67%

========================= 7 passed, 1 warning in 2.74s =========================

<img width="378" alt="TESTCASES" src="https://user-images.githubusercontent.com/9552989/76163792-26350980-6141-11ea-8483-28038e5b5a55.PNG">

# Evaluation  

Overall I would consider this project to be a success. The application is functional and my CI pipeline works seamlessly to deploy the application. Moving forward, however, I would definitely work to build a more complicated and visually pleasing application. I had my MVP (Minimum Viable Product) in mind during the creation due to the time constraint. This being said, I am still happy with the final product. 

