def rps_comp(ai_choice, user_choice):
    if ai_choice == user_choice:
        return "you tied"
    if user_choice == "paper":
        if ai_choice == "scissors":
            return "you lost"
        if ai_choice == "rock":
            return "you won"
    if user_choice == "scissors":
        if ai_choice == "rock":
            return "you lost"
        if ai_choice == "paper":
            return "you won"
    if user_choice == "rock":
        if ai_choice == "paper":
            return "you lost"
        if ai_choice == "scissors":
            return "you won"