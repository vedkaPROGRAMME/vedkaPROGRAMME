import random
for i in range(1,101):
    print(i)
    if i%5==0 and i%3==0:
        print("Fizz")
    elif i%3==0:
        print("Buzz")
    elif i%5==0:
        print("FizzBuzz")
    else:
        print("number")
