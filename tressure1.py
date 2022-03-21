print("Welcome to the tressure islland .")
print("Your mission is to find tressure.")
choice1 = input("please choice between right and left ?").lower()
if choice1 == "left":
    print("You have passed this step . You need to go to the island")
    choice2 = input("Please select you wanna wait or pass it by swim .").lower()
    if choice2 == "wait":
        print("You passed this step alive . Welcome to the next step .")
        choice3 = input("there are three doors in the house . Please select between one of them . Doors are red , green and yellow.").lower()
        if choice3 == "red":
            print("This room is full of fire . You are dead. GAME OVER.")
        elif choice3 == "green":
            print("This room is door to the hell. You arae dead. GAME OVER")
        elif choice3 == "yellow":
            print("You selected right door . Tressure is all yours. YOU WIN")
            print('''*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************''')
        else:
            print("You selected wrong answer.")
    else:
        print("water is full of sharks and deadly sea animals .You are dead.game over.")
    
    
else:
    print("You failed . GAME OVER.")
    




