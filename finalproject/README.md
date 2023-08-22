#Voting Application Documentation#

This documentation describes the voting application developed by Brandon Michel Caldarella. The application is designed to allow users to create surveys and polls, and for participants to cast their votes on different options. This application was developed using the Django framework, Javascript, HTML5, and CSS3. It is intended to facilitate decision-making and the collection of user opinions on various topics.
--------------
#Motivation

The decision to create this voting application was driven by several fundamental reasons:

⦁ **Application of Knowledge:** This application was conceived as a project to apply the knowledge gained from the CS50's Web Programming with Python and Javascript course. The application encompasses a wide range of concepts, from creating models and views to implementing user authentication and handling multimedia files. It is considered an opportunity to showcase the skills and understanding of key concepts learned in this course.

⦁ **Need for Opinion Collection:** In everyday life, understanding the opinions of the people around us is essential for making informed decisions. This application addresses the need to gather and comprehend user opinions on various topics. It facilitates the creation of surveys and polls, thereby providing a clear insight into the preferences and viewpoints of a group of individuals.

⦁ **Differentiation** from Other Projects: This application sets itself apart from previous projects due to its unique nature. While users can interact with each other, the application does not resemble a social network or an e-commerce platform. Its core functionality revolves around creating and participating in surveys and polls. This enables informed decision-making on diverse issues and distinguishes it from prior approaches focused on social media and e-commerce.

------------
#Key Features
• Creation and management of surveys and polls.

• Options to provide detailed descriptions and add images to each voting choice.

• User authentication to ensure proper participation and access.

• Implementation of access codes to control which users are authorized to participate in a survey or poll.

• Visualization of voting results, including the most voted options.

• Functionality to inform users whether they have already cast their vote in a specific poll.

• Ability to set a closing date for polls and automatically close them after that date.

---------------
#Application Code

The provided code is the complete implementation of the voting application developed in Django. It includes the necessary models, views, and forms for the proper functioning of the application. Below are some of the key components of the code:

Models

• **User:** Extended user model derived from the AbstractUser model provided by Django to include additional profile information.

• **Profile:** Model to store additional user profile information such as first name, last name, and profile picture.

• **Create_vote:** Model to represent a voting poll or survey created by a user. It includes details such as the poll's name, description, associated image, selected option, and the poll's status.

• **VoteOption:** Model that defines individual voting options, including option text, description, and image.

-------------
Views

• **index:** Displays all available polls on the homepage.


• inprogress: Displays ongoing polls, with options to search for specific polls.

• **description:** Displays the description of a poll and requests an access code if configured.

• **voting_view:** Allows users to cast their vote on a specific voting option.

• **voting_results:** Displays the results of a poll, including vote percentages for each option.

• **voting_users:** Returns a JSON response containing information about users who have voted in a specific poll.

• **profile:** Displays a user's profile, along with the ability to create new polls.

• **edit_profile:** Allows users to edit their profile, including the profile picture.

• **new_survey:** Allows users to create a new poll or survey with associated options and details.

• **mychoose:** Displays voting options chosen by a user.

• **vote:** Displays polls created by the current user.

• **deleteVote:** Deletes a specific poll created by the user.

• **editVote:** Allows users to edit an existing poll, including options and associated details.

• **change_status:** Changes the status of a poll to "closed" if the closing date has passed.

• **close_vote:** Manually closes a poll if the creator decides to do so.

• **more_votes:** Displays voting options with the most votes in a closed poll.

• **Login_view:** Handles login authentication.

• **register:** Handles the registration of new users.

• **logout_view:** Handles user logouts.

Additional Functions

• **create_user_profile:** A post_save signal receiver that automatically creates a profile for a newly registered user.

• **close_expired_votes:** A function that runs in a separate thread to automatically close polls that have reached their closing date.

• Use of HTML templates to render pages and display information to users.
---------------
#Conclusions

The developed voting application offers an effective way to gather opinions and make informed decisions on a variety of topics. By applying the knowledge gained in this course, a robust and comprehensive implementation of the necessary functionalities for creating, participating in, and managing surveys and polls is achieved. This documentation provides an overview of the motivation behind the application, its key features, and how it has been implemented.

----------
#Getting Started

If you don't have python installed, install it, this app is made with Python version 3.9.13

Open a terminal and navigate to the location of the directory that contains the application code.

In your terminal, cd into the finalproject directory.

Run **python3 manage.py** makemigrations  to make migrations for the wishes app.

run **python3 manage.py** migrate to apply migrations to your database.

run **python3 manage.py** runserver to run the app




