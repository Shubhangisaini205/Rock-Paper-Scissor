import random
choiceslist = ["rock","scissor","paper"]



while True:
    Ccount = 0
    Ucount = 0
    userChoice = int(input('''
 Game Start..... 
 1 Yes
 2 NO | Exit

    '''))
    if userChoice==1:
        for a in range(1,6):
            userInput=int(input('''
1 Rock
2 Scissor
3 Paper 

              '''))
            if userInput==1:
                uChoice = "rock"
            elif userInput==2:
                uChoice="scissor"
            elif userInput==3:
                uChoice="paper"
            Cchoice = random.choice(choiceslist)
            # print(uChoice)
            # print(Cchoice)
            if Cchoice==uChoice:
                print("Computer Value:", Cchoice)
                print("User Value:", uChoice)
                print("Game Draw")
            elif (uChoice=="rock" and Cchoice=="scissor") or  (uChoice=="paper" and Cchoice=="rock")  or (uChoice=="scissor" and Cchoice=="paper"):
                print("Computer Value:", Cchoice)
                print("User Value:", uChoice)
                print("You Win")  
                Ucount= Ucount + 1
            else:
                print("Computer Value:", Cchoice)
                print("User Value:", uChoice)
                print("Computer Win")
                Ccount= Ccount + 1


        if Ucount==Ccount:
            print("Final Game Draw....")
            print("User Score", Ucount)
            print("Computer Score", Ccount)
        elif Ucount>Ccount:
            print("Final You Win the Game....")
            print("User Score", Ucount)
            print("Computer Score", Ccount)
        else:
            print("Final Computer Win the Game....")
            print("User Score", Ucount)
            print("Computer Score", Ccount)  

    else:
        break