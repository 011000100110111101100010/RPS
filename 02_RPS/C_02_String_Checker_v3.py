# Checks that users have entered a valid option on a list
def string_checker(question, valid_ans=("yes", "no")):
    error = f"Please enter a valid option from the following list{valid_ans}"
    while True:
        # gets the user response and makes it lowercase
        user_response = input(question).lower()

        for item in valid_ans:
    # checks if the user response is in the word list
            if item == user_response:
                return item

        #checks if the user response is the same as the first letter of an item in a list
            elif user_response == item[0]:
                return item

        # prints error if user enters somthing invalid
        print(error)
        print()
# main routine goes here

yes_no = ["yes", "no"]
rps_list = ["rock", "paper", "scissors", "xxx"]

want_instructions = string_checker("do you want the instructions?")

print("you chose", want_instructions)

user_choice = string_checker("choose:", rps_list)
print("you chose:",user_choice)