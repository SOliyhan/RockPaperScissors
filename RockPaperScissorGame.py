import random

print("Welcome to a Game of Rock Paper Scissors\n")
rounds=int(input("How many rounds would you like to play: "))
player_score,computer_score=0,0
phrase=''

moves=['rock','paper','scissors']

for game_round in range(rounds):
    print("Round: ",str(game_round+1))
    print("Player: ",str(player_score),"\t\tComputer: ",str(computer_score))
    player_choice=input("Time to pick.... rock, paper, scissors: ").lower()

    #random choice selection for computer
    computer_index= random.randint(0,2)
    computer_choice=moves[computer_index]

    if player_choice in moves:
        print("\tComputer: ", computer_choice)
        print("\tPlayer: ", player_choice)

        if computer_choice==player_choice:
            winner='tie'
        elif computer_choice=='rock':
            if player_choice=="paper":
                winner='player'
                phrase="Paper covers Rock!"
            elif player_choice=="scissors":
                winner = 'computer'
                phrase = '\tRock breaks Scissors!'
        elif computer_choice=='paper':
            if player_choice=='rock':
                winner='computer'
                phrase="\tPaper covers Rock!"
            elif player_choice=='scissors':
                winner='player'
                phrase="\tScissors cut Paper!"
        elif computer_choice=='scissors':
            if player_choice=='paper':
                winner='computer'
                phrase="\tScissors cut Paper!"
            elif player_choice=='rock':
                winner='player'
                phrase='\tRock breaks Scissors!'

        if winner=="computer":
            print(phrase)
            print("\tComputer win round ",game_round+1)
            computer_score+=1
        elif winner=="player":
            print(phrase)
            print("\tPlayer win round ",game_round+1)
            player_score+=1
        elif winner=="tie":
            result = "\tIt is a tie, how boring!\n\tThis round was a tie."
            print(result)
    else:
        print("\tInvalid game option!")
        print("\tComputer gets the point.")
        computer_score += 1

#displaying result
print(f"\n-------------Results------------- \nRounds played:{str(rounds)}"
      f"\n\tComputer Score: {computer_score}      Player Score: {player_score}")
if computer_score>player_score:
    print("\n\tComputer wins more rounds!! :-(")
elif computer_score<player_score:
    print("\n\tHurray! Player wins more rounds!!")
else:
    print("\n\tThe game was a tie.")






