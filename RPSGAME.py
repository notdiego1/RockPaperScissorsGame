from random import choices

def scoreBoard(player,score):
    global total1
    global total2
    if player == "player1":
        total1 = total1 + score
    elif player == "player2":
        total2 = total2 + score
    print("Player1: ", total1, " and Player2: ", total2)

def finalScore(total1,total2):
    if total1 > total2:
        print("Player1 is the winner!")
    elif total1 < total2:
        print("PLayer2 is the winner!")
    else:
        print("We have a tie!")

def Game(value1,value2):
    print ("Player 1: " + value1.capitalize() + "\nPlayer 2: " + value2.capitalize())
    options = ["paper","rock","scissors"]
    if (value1 or value2) not in options:
        print ("Please enter a correct value.")
    else:
        #Rock and Scissors are the first ones up.
        if (value1 == "rock") and (value2 == "scissors"):
            print("Rock beats Scissors. Player 1 wins this round.")
            scoreBoard("player1",1)
        
        elif (value2 == "rock") and (value1 == "scissors"):
            print("Rock beats Scissors. Player 2 wins this round.")
            scoreBoard("player2",1)

        #Rock and Paper now.
        elif (value1 == "rock") and (value2 == "paper"):
            print("Paper beats Rock. Player 2 wins this round.")
            scoreBoard("player2",1)
        
        elif (value2 == "rock") and (value1 == "paper"):
            print("Paper beats Rock. Player 1 wins this round.")
            scoreBoard("player1",1)

        #Scissors and Paper now.
        elif (value1 == "scissors") and (value2 == "paper"):
            print("Scissors beats Paper. Player 1 wins this round.")
            scoreBoard("player1",1)
    
        elif (value2 == "scissors") and (value1 == "paper"):
            print("Scissors beats Paper. Player 2 wins this round.")
            scoreBoard("player2",1)

        #Tie.
        else:
            print ("Tie this round. No winner.")

#Main
total1= 0
total2= 0
print ("\tRock, Paper, Scissors Game.")
value1 = input("Please enter Rock, Paper, or Scissors: ").strip(" ").lower()

npcmoveList = ["paper", "rock", "scissors"]
value2 = choices(npcmoveList)

Game(value1, value2[0])

def repeatRound():
    i = input("Would you like to go again?(y/n) ").strip(" ").lower()
    if i in ["y","yes"]:
        while i in ["y","yes"]:
            value1 = input("\nPlease enter Rock, Paper, or Scissors: ").strip(" ").lower()
            value2 = choices(npcmoveList)
            Game(value1, value2[0])
            repeatRound()
            break
    elif i in ["n","no"]:
        print ("\nGood Game:)")
        finalScore(total1,total2)
    else:
        print("Please enter a correct value.")
        repeatRound()
repeatRound()