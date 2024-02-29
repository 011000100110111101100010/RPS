# initialize variables
import random

rounds_played = 0
mode = 0
rounds_won = 0
rounds_lost = 0
rounds_tied = 0
game_history = []


# Checks that users have entered a valid option on a list
def string_checker(question, valid_ans):
    error = f"Please enter a valid option from the following list{valid_ans}"
    while True:
        # gets the user response and makes it lowercase
        user_response = input(question).lower()

        for item in valid_ans:
            # checks if the user response is in the word list

            if item == user_response:
                return item

            # checks if the user response is the same as the first letter of an item in a list

            elif user_response == item[0]:
                return item

        # prints error if user enters somthing invalid
        print(error)
        print()


# displays the instructions
def instructions_text():
    print('''
    
    ✊✌️✋ Instructions ✊✌️✋
    
To begin, choose the number of rounds (or press <enter> for infinite mode).
Then play against the computer. YOu can choose between R (rock), P (paper) or S (scissors).
The rules are as follows:
- Paper beats rock
- Rock beats scissors
- Scissors beats paper
Type <quit> to end the game at anytime.
    
    ''')


# checks if the integer is infinite or more than one
def int_checker(question):
    error = "please enter an integer above 1"
    while True:
        value = input(question)
        if value == "":
            return ""

        try:
            intvalue = int(value)

            if intvalue > 1:
                return intvalue

            else:
                print(error)

        except ValueError:
            print(error)


def ai_move(choices):
    return random.choice(choices)


def rps_comp(ai, user):
    if ai == user:
        return "tie"
    if user == "paper" and ai == "scissors" or user == "scissors" and ai == "rock" or user == "rock" and ai == "paper":
        return "lose"
    if user == "paper" and ai == "rock" or user == "scissors" and ai == "paper" or user == "rock" and ai == "scissors":
        return "win"


print("✊✌️✋ Rock / Paper / Scissors ✊✌️✋")
print()

want_instructions = string_checker("Do you want to read the instructions? ", ("yes", "no"))

if want_instructions == "yes":
    instructions_text()

round_num = int_checker("how many rounds would you like to play to press enter for infinite")
# sets the mode to infinite
if round_num == "":
    mode = "Infinite"
    round_num = 20
else:
    mode = "Normal"


while round_num > rounds_played:
    rounds_played += 1
    round_heading = f"\nRound {rounds_played} ({mode} mode)"
    print(round_heading)
    user_choice = string_checker("choose: ", ("rock", "paper", "scissors", "xxx"))
    print("you chose: ", user_choice)

    # creates a way of breaking out of the loop
    if user_choice == "xxx":
        if rounds_played == 1:
            print("cannot skip pass on round 1")
        else:
            rounds_played -= 1
            break

    ai_choice = ai_move(["rock", "paper", "scissors"])

    print("ai chose: ", ai_choice)
    game = rps_comp(user_choice, ai_choice)
    print("you", game)

    # adjust game stats and history
    if game == "won":
        rounds_won += 1
    elif game == "lose":
        rounds_lost += 1
    else:
        rounds_tied += 1

    if mode == "Infinite":
        round_num += 10
    game_history.append(game)
percent_won = (rounds_won / rounds_played) * 100
percent_lost = (rounds_lost / rounds_played) * 100
percent_tied = (rounds_tied / rounds_played) * 100
print(f"\nyou tied {percent_tied}% of the time")
print(f"\nyou lost {percent_lost}% of the time")
print(f"\nyou won {percent_won}% of the time")
print(f"\nyou played {rounds_played} games")
print("game history: ", game_history)
