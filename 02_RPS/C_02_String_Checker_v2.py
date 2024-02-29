# Checks that users have entered a valid option on a list
def string_checker(user_response, valid_ans):
    while True:
        # gets the user response and makes it lowercase
        user_response = user_response.lower()

        for item in valid_ans:
    # checks if the user response is in the word list
            if item == user_response:
                return item

        #checks if the user response is the same as the first letter of an item in a list
            elif user_response == item[0]:
                return item

        return "invalid"

# automated testing is below in the form (test_case, expected_value)
to_test = [
    ("PAPER", "paper"),
    ("scissors", "scissors"),
    ("R", "rock"),
    ("P", "paper"),
    ("XXX","xxx"),
    ("x", "xxx"),
    ("random", "invalid"),
]

# run tests!
for item in to_test:
    # retrieve test case and expected values
    case = item[0]
    expected = item[1]

    # get actual value (ie: test ticket function)
    actual = string_checker(case, ["rock", "paper", "scissors", "xxx"])

    # compare actual and expected and output pass / fail
    if actual == expected:
        print(f"✅✅✅Passed! Case: {case}, expected: {expected}, received: {actual}✅✅✅")
    else:
        print(f"❌❌❌ Failed! Case: {case}, expected {expected}, received, {actual}❌❌❌")