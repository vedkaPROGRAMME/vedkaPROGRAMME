import random
print("Hey there, welcome to the game .")
toss = input("Its time for  the toss. Select T for tails and H for heads.")
random.seed()
computer_choice = random.randint(0,1)
if computer_choice == 0:
    print("H")
else:
    print("T")
if computer_choice == toss:
    print("YOU WON THE TOSS")
else:
    print("You lost the toss!")
    select = input("Please select you wanna bat or ball . Type B for bat and b for ball.")
    if select == 'B':
        kohli = input("Please select which type of ball do you want ? 1 for bouncer or 2 for yorker.")
        if kohli == 1:
            bumrah =input("You hit the ball out of ground!Now prepare of second ball. type 3 for faster or 4 for slower.")
            if bumrah == 3 :
                raina = input("You hit the ball for two runs. here 3rd ball is coming . type 5 for left spin or 6 for right spin .")
                if raina == 5 :
                    print("You hit the ball straight. There you go .Game is over!")
                else:
                    print("You hit the ball in hands. Thats the wicket.Total score is . . Game is over!")
            else:
                print("You hit the ball at mid-wicket. one run. ")
        else:
            print("Whattta defend !!! No run on this ball.")
    else :
        jaddu = input("You took the ball. Its time to show some spin. select 0 for slower or  1 for bouncer or 2 for yorker.")
        auto1 = random.randint(0,2)
        if auto1 == 0:
            print("User hit the ball for six!!!")
        elif auto1 == 1 :
            print("User hit the ball on long off. Two runs.")
        else:
            faf = input("User hit the ball on cover. No runs.Now go for second ball . select 0 for faster or 1 for lower.")
            auto2 = random.randint(0,1)
            if auto2 == 0:
                dhoni = input("Ball goes for four runs. Here you go for third ball. select 4 for inswing or 5 for outswing.")
                if dhoni == 5:
                    print("ball is in the  hands . User is out.")
                else:
                    print("user shoot helicopter shot. you win the game .")
            elif auto2 == 1 :
                rohit ==input("Ball is in stand !!! Here you go for third ball . select 4 for inswing or 5 for outswing ")
                if rohit == 4:
                    print("Ball is over long on. throw before user takes two runs.")
                else:
                    print("User missed the ball .You won the game .")
                
                
                    
