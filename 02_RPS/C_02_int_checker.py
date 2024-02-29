#checks if the integer is infinite or more than one
def int_checker(question):
    error = "please enter an integer above 0"
    while True:
        value = input(question)
        if value == "":
            return "infinite"

        try:
            intvalue = int(value)

            if intvalue > 0:
                return intvalue

            else:
                print(error)

        except ValueError:
            print(error)


score = int_checker("go")
print(score)
