print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
name3 = name1 + name2
lower_case_latter = name3.lower()
l = lower_case_latter.count("l")
o = lower_case_latter.count("o")
v = lower_case_latter.count("v")
e = lower_case_latter.count("e")
love = l+o+v+e
t = lower_case_latter.count("t")
r = lower_case_latter.count("r")
u = lower_case_latter.count("u")
e = lower_case_latter.count("e")
true = t+r+u+e
love_score = (true)+(love)
print(love_score)
if (love_score < 10) or (love_score> 90):
    print(f"Your score is {love_score}%, you go together like coke and mentos.")
elif (love_score > 40) or (love_score < 90):
    print(f"Your score is {love_score}%, you are alright together.")
else:
    print(f"Your score is {love_score}.")
