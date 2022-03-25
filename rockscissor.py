import random
rock = '''
    _______
---  ____)
      (_____)
      (_____)
      (____)
---.__(___))'''
paper = '''
    _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)),'''
scissor ='''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)'''
game = [ rock , paper , scissor]

auto = int(input("please select your choice ! 0 for rock , 1 for paper, 2 for scissors."))
if auto >= 3 or auto < 0 :
    print("You slected wrong input!")
else:
    print(game[auto])
computer_choice = random.randint(0,2)
print("computer choices:")
print(game[computer_choice])
if auto >= 3 or auto < 0 :
    print("You slected wrong input!")
elif computer_choice == auto :
    print("Its draw!!")
elif auto == 2 and computer_choice == 0 :
    print("You loose!")
elif auto == 0 and computer_choice == 2 :
    print("You win!")
elif computer_choice > auto :
    print("You loose!")
elif auto > computer_choice:
    print("You win!")

    

             
    
