def playgame():
    print("Hello Welcome to the game \n" + ("rock-paper-scissors").upper())
    usr = input("\nInput'yes or no'only... \nAre you ready?:")
    if usr == "yes":
        users_name = (str(input("\nYour name:"))).title()
        number_of_rounds = int(input("\nDear" + " " +users_name +"," +" " +"Goodluck!...on your current trial of the game "+ "please input the number of rounds you wish to play below...\nNote:the value must be an integer else the program will raise an error"+ "\n\nThe number of rounds you wish to play:"))
        users_score = 0
        computers_score = 0
        print("\nNote in this game your choice of play should be either of (rock,paper,scissors)\nPlaying anything outside that will raise an error in the program...\nSpelling mistakes and wrong use of case will also cause errors")
        for i in range(number_of_rounds):
            from random import choice
            chance = ("rock","paper","scissors")
            computers_turn = choice(chance)
            print((("\nRound"+ " " + str(i + 1))).upper())
            if i+1 == number_of_rounds:
                print("Last Round!")
            users_turn = input("\nDear"+ " " + users_name+"\nIts your turn...\nPlay:")
            print("Computers_turn:...The computer played;" +computers_turn + "\n")
            if (users_turn == "rock" and computers_turn == "scissors") or (users_turn == "paper" and computers_turn == "rock") or (users_turn == "scissors" and computers_turn == "paper"):
                users_score += 1
                print("Won!...", "your", users_turn, "defeated" ,"the computers", computers_turn )
                print("Current scores" + "("+ users_name + " vs computer):" + str(users_score)+"-"+ str(computers_score) )
                if computers_score > users_score:
                    print("Dear"+ " " +users_name +"," + "Strive harder, you are currently losing to the computer...")
                elif users_score > computers_score:
                    print("Dear" + " " + users_name +","+ "Keep it up,you are leading")
                else :
                    print("Dear" + " " + users_name +"," +" You can do better...its a draw for now...")
            elif(users_turn == "rock" and computers_turn == "paper" ) or (users_turn == "paper" and computers_turn == "scissors") or (users_turn == "scissors" and computers_turn == "paper"):
                computers_score += 1
                print("Lost!", "your", users_turn, "was defeated by the computers", computers_turn)
                print("Current scores" + "("+ users_name + " vs computer):" + str(users_score)+"-"+ str(computers_score) )
                if computers_score > users_score:
                    print("Dear"+ " " +users_name +"," + "Strive harder, You are currently losing to the computer...")
                elif users_score > computers_score:
                    print("Dear" + " " + users_name +","+ "Keep it up,you are leading")
                else :
                    print("Dear" + " " + users_name +"," +" you can do better...its a draw for now...")
            elif users_turn == computers_turn:    
                print("A draw...", "your", users_turn, "is the same thing as the computer's", computers_turn)
                print("Current scores" + "("+ users_name + " vs computer):" + str(users_score)+"-"+ str(computers_score) )
                if computers_score > users_score:
                    print("Dear"+ " " +users_name +"," + "Strive harder, you are currently losing to the computer...")
                elif users_score > computers_score:
                    print("Dear" + " " + users_name +","+ "Keep it up,you are leading")
                else:
                    print("Dear" + " " + users_name +"," +" You can do better...its a draw for now...")
        print(("\nEnd of game...\n").upper())
        if computers_score > users_score:
            print("Score;" +"("+ users_name , "vs computer" +"):"+" "+  str(users_score) +"-"+ str(computers_score))
            print("Dear " + users_name + "," +"you lost this game to the computer,better luck next time!,bye!")
        elif computers_score < users_score:
            print("Score;"+"("+ users_name , "vs computer" +"):"+" "+  str(users_score) +"-"+ str(computers_score))
            print("Dear"+ " " + users_name + "," + "you won this game,congrats!")
        elif computers_score == users_score:
            print("Score;"+"("+ users_name , "vs computer" +"):"+" "+  str(users_score) +"-"+ str(computers_score))
            print("Dear" + " " + users_name +"," +"its a draw, you had the same score with the computer.better luck next time!")
    elif usr == "no":
                print("bye!,try when you are ready")  
    else:
        print("invalid input'available options are; yes or no'\ntry reopening the game again, bye for now!")
playgame()