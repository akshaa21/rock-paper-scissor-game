import random
l=["rock","paper","scissor"]
'''
 rock vs paper -> paper wins 
 rock vs scissor -> rock wins
 scissor vs paper -> scissor wins 
'''

while True:
    ccount = 0
    ucount = 0 
    userc = int(input(''' 
Game Start.......
1 YES
2 NO | Exit 
Enter your choice:                  
                  ''')) 
    
    if userc == 1:
        for a in range(1,6):
            userInput = int(input(''' 
Select any one option...
1 Rock
2 Paper
3 Scissor                              
                                  '''))
            if userInput == 1:
                uchoice = "rock"
            elif userInput == 2:
                uchoice = "paper"
            elif userInput == 3:
                uchoice = "scissor"
            Cchoice = random.choice(l)
            if Cchoice == uchoice:
                print("User Value -->",uchoice)         
                print("Computer Value -->",Cchoice)
                print("Game Draw")
                ucount = ucount + 1
                ccount = ccount + 1
            elif (uchoice == "rock" and Cchoice == "scissor") or (uchoice == "paper" and Cchoice == "rock") or (uchoice == "scissor" and Cchoice == "paper"):
                print("User Value -->",uchoice)         
                print("Computer Value -->",Cchoice)  
                print("You Win")
                ucount = ucount + 1
            else:
                print("User Value -->",uchoice)         
                print("Computer Value -->",Cchoice)        
                print("Computer Win")
                ccount = ccount + 1
        print("\n")   
        print("==============================================================================================================================")
        print("\n")       
        if ucount == ccount:
            print("Final Result ---> Game Draw")
            print("User Score =",ucount)
            print("Computer Score =",ccount)
            print("\n")   
            print("Want To Play Again.....")
        elif ucount > ccount:
            print("Final Result ---> You Win The Game")
            print("User Score =",ucount)
            print("Computer Score =",ccount)
            print("\n")    
            print("Want To Play Again.....")
        else:
            print("Final Result ---> Computer Win The Game")
            print("User Score =",ucount)
            print("Computer Score =",ccount)  
            print("\n")    
            print("Want To Play Again.....")           
    else:
        break        
