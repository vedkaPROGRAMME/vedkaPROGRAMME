height = float(input("enter your height:"))
weight = float(input("enter your weight:"))
bmi = round(weight/height**2)
if bmi < 18.5 :
    print("Your bmi is", bmi,", you are underweight.")
elif bmi < 25 :
    print("Your bmi is", bmi,", you have a normal weight.")
elif bmi < 30 :
    print("Your bmi is", bmi,", you are slightly overweight.")
elif bmi < 35 :
    print("Your bmi is", bmi,", you are obsese.")
else:
    print("Your are clinically obese")
