# import pyfiglet module for ascii art
import pyfiglet

def welcome():
    """
    Title & welcome message
    """
    title = pyfiglet.figlet_format(
        "NBA QUIZZ", font="standard", justify="center")
    print(title)

# ------------------
def new_game():
    
    name_data = input("Enter your name here to begin:\n")
    guesses = []
    correct_guesses = 0
    question_num = 1

    for key in questions:
        print("-------------------------------")
        print(key)
        for i in options[question_num-1]:
            print(i)
        guess = input("Enter (A, B, C or D): ")
        guess = guess.upper()
        guesses.append(guess)

        correct_guesses += check_answer(questions.get(key),guess)
        question_num += 1

    display_score(correct_guesses, guesses)
        

# ------------------
def check_answer(answer, guess):
    
    if answer == guess:
        print("That is the right answer =)")
        return 1
    else:
        print("That is the wrong answer =(")
        return 0
# ------------------
def display_score(correct_guesses, guesses):
    print("-------------------------------")
    print("RESULTS")
    print("-------------------------------")

    print("Answers:")
    for i in questions:
        print(questions.get(i), end=" ")
    print()

    print("Guesses:")
    for i in guesses:
        print((i), end=" ")
    print()

    score = int((correct_guesses/len(questions))*100)
    print("Your score is: "+str(score)+"%")
# ------------------
def play_again():
    
    response = input("Do you want to play again? (Yes or No?): ")
    response = response.upper()

    if response == "YES":
        return True
    else:
        return False




questions = {
    "Michael Jordan played with what number for Chicago Bulls?": "A",
    "Wich team was Lebron James first team?": "B",
    "What year was nba invented?": "D",
    "Who won 2022 nba championship?": "D",
}

options = [["A. 23", "B. 24", "C. 25", "D. 26"],
          ["A. Lakers", "B. Cleveland", "C. Miami", "D. Bucks"],
          ["A. 1944", "B. 1945", "C. 1947", "D. 1946"],
          ["A. Lakers", "B. Boston", "C. Bulls", "D. Warriors"]]

new_game()

while play_again():
    new_game()

print("Have a nice day!")
