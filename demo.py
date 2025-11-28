import random
def computer_choice():
    choices = ["Rock","Paper","Scissor"]
    return random.choice(choices)

valid_input = ["Rock", "Paper", "Scissor"]

user_score = 0
computer_score = 0

while True:
    print("Welcome to the World of Games!")
    print("Choose your desired choice:")
    print("Rock")
    print("Paper")
    print("Scissor")

    user_choice = input("Enter your choice:").capitalize().strip()
    comp = computer_choice()

    if user_choice not in valid_input:
        print("Invalid Input, Please Try Again")
        continue

    print(f"You chose: {user_choice}")
    print(f"Computer chose: {comp}")

    if user_choice == comp:
        print("Result: Draw")
    elif (user_choice == "Rock" and comp == "Paper") or\
         (user_choice == "Scissor" and comp == "paper") or\
         (user_choice == "Rock" and comp == "Scissor"):
        print("Result: You win ✅")
        user_score +=1
    else:
        print("Result: Computer Wins ❌")
        computer_score +=1
    
    print(f"Score BOARD:")
    print(f"You : {user_score} | Computer: {computer_score}")

    play_again = input("Do you want to play again? (yes/no)").lower()
    if play_again == "no":
        print("Final Score")
        print(f"You: {user_score} | Computer: {computer_score}")

        if user_score > computer_score:
            print("🏆 You are the final Winner!🏆")
        elif computer_score > user_score:
            print("💻Computer is the final Winner😅")
        else:
            print("🤝Match Tied!")
        
        print("Thanks for plaiyng!")
        break