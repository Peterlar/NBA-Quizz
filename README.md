# **NBA QUIZZ**

NBA Quizz, is a Python terminal game that runs on Heroku.

View the live project [Here](https://nbaquizz.herokuapp.com)

Users will get a sample of questions with multiple answer selections and different difficulty levels. The game should contain questions from different timelines to maintain a intresseting level making the user have to search for the answers and learn more about NBA and capture an interest of the fantastic sport basketball.

![image](https://user-images.githubusercontent.com/100356636/179196042-9378f584-9e41-4667-bef4-b0798d8e554d.png)

# *How to play?*

NBA Quizz is based from the different quizzes you will se every week from the different sportschannels and socialmedia that covers mayor sports events.
When you enter the app you must enter your name and you will be directed to the first question. You will then have 4 different options to choose from. A, B, C, or D.
Choose one of the answers and then hit "ENTER". The player will be notified with an message if the answer is correct or not.
The guesses will be gathered in the end of the quizz and the right answers will be available. The player will recive and procentage showing how many guesses was right and then asked if you want to try again. 

# **Features**

* Ascii design on the logo ( NBA QUIZZ ).

![image](https://user-images.githubusercontent.com/100356636/179201570-ea226adf-08ab-4c36-8d97-d8a5e6cd22e3.png)

* Enter your name to start the game.

![image](https://user-images.githubusercontent.com/100356636/179202722-750f3210-3c59-4b97-9127-df6585c5b326.png)

* Questions with multiple answers. Player will be notified with an message if the answer is correct or not.

![image](https://user-images.githubusercontent.com/100356636/179208078-cc31b025-306e-455f-aca1-31253ebf6a68.png)

# **Deployment**

The site was deployed via Heroku.
This project was developed utilising the Code Institute Template. 

Before deploying to Heroku pip3 freeze > requirements.txt was used to add pyfiglet for deployment.

* Results will show the guesses from the player and the correct answers. Below an procentage will be visible displaying the score. Player will also be able to play again by answering "YES" or "No" and then hit enter. If player enters "NO" and message will occur or the game restarts from the beginning.

![image](https://user-images.githubusercontent.com/100356636/179210332-38ce30c7-5920-49c7-8077-3e5ff9f36bb3.png)

**Future Features:**
* Weekly new questions
* Highscore List
* NBA Highlights of the week.

# **Libraries & Technology Used**

* Pyfiglet for adding ascii art.


# **Testing**

I have manually tested this project by doing:

* Passed the code through a PEP8 linter and confirmed there are no problems.
* Tested in my lokal terminal and the Code Institute Heroku Terminal.
* Tested the game after each question was added to check it worked.

**Bugs**

* During the project i was getting type of errors that was caused by not have entered enough blankspaces. It was solved during the PEP8 linter testing.

![image](https://user-images.githubusercontent.com/100356636/179350205-58a01b94-3ffe-4700-ba32-661d67e3bc72.png)

# **Deployment**

The site was deployed via Heroku. This project was developed utilising the Code Institute Template.

Before deploying to Heroku pip3 freeze > requirements.txt was used to add pyfiglet for deployment.

1.	Log in to [Heroku]( https://id.heroku.com/login) or create an account if required.
2.	Then, click the button labelled **New** from the dashboard in the top right corner and from the drop-down menu select **Create New App**.
3.	You must enter a unique app name, (I used mastermind-code-breaker).
4.	Next, select your region, (I chose Europe as I am in Sweden).
5.	Click on the **Create App** button.
6.	The next page you will see is the project’s Deploy Tab.  Click on the **Settings Tab** and scroll down to **Config Vars**.
7.	Next, scroll down to the Buildpack section click **Add Buildpack** select **python** and click **Save Changes**.
8.	Repeat step 8 to add **node.js**.
o	**Note:** The Buildpacks must be in the correct order. If not click and drag them to move into the correct order.
9.	Scroll to the top of the page and now choose the **Deploy** tab.
10.	Select **Github** as the deployment method.
11.	Confirm you want to connect to GitHub.
12.	Search for the repository name and click the connect button.
13.	Scroll to the bottom of the deploy page and select preferred deployment type:

* Click either **Enable Automatic Deploys** for automatic deployment when you push updates to Github.


* Select the correct branch for deployment from the drop-down menu and click **Deploy Branch** for manual deployment.

# **Credits**

* During this project i was watching different tutorials to get ideas and help with the coding. I want to say thanks to " Mike Dane" and " Bro Code " for great tutorials. 

* I also want to say thanks to my mentor Daisy Mc Girr for great help and tools during this project.

* Tutor support has also as always been a great help during this project and the slack community that helped me with the ascii art coding.
