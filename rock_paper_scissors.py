import random

def comp_choice():
    return random.choice(['rock','paper','scissors'])

def check(comp_choice, user_choice):
    if(comp_choice==user_choice):
        return "It's a tie.."
    elif((comp_choice=='rock' and user_choice=='paper') or
         (comp_choice=='paper' and user_choice=='scissors') or
         (comp_choice=='scissors' and user_choice=='rock')):
        return "It's a win!!"
    else:
        return "It's a loss!!"
    
def main():
    print("Welcome to the Game!!")

    comp_score=0
    user_score=0

    while True:
        gamer_choice=input("Enter your choice(rock, paper, scissors): ").lower()
        if gamer_choice not in ['rock','paper','scissors']:
            print("Enter a valid choice...")
            continue

        computer_choice=comp_choice()
        print("Computer choice is ",computer_choice)

        result=check(computer_choice, gamer_choice)

        if(result=="It's a loss!!"):
            comp_score+=1
        elif(result=="It's a win!!"):
            user_score+=1

        print("Gamer score: ",user_score,"Computer score: ",comp_score)

        play_again=input("You want to play again?(y/n): ").lower()
        if(play_again!='y'):
            break
    print("Thanks for playing..")

if __name__=="__main__":
    main()
        