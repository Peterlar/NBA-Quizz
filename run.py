# ------------------
def new_game():
    
    guesses = []
    correct_guesses = 0
    question_num = 1

    for key in questions:
        print(key)
# ------------------
def check_answer():
    pass
# ------------------
def display_score():
    pass
# ------------------
def play_again():
    pass


questions = {
    "Michael Jordan played with what number for Chicago Bulls?": "A",
    "Wich team was Lebron James first team?": "B",
    "What year was nba invented?": "D",
    "Who won 2022 nba championship?": "D",
}

options = [["A. 23", "B. 24", "C. 25", "D. 26"],
          ["A. Lakers", "B. Cleveland", "C. Miami", "D. Bucks"],
          ["A. 1944", "B. 1945", "C. 1947", "D. 1946"],
          ["A. Lakers","B. Boston", "C. Bulls", "D. Warriors"]]

new_game()