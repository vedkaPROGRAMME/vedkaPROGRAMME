age = input("What is your current age?")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
aget = int(age)
years_left = 90 - aget
months_left = years_left*12
weeks_left = years_left*52
days_left = years_left*365
total = f"You have {days_left} days, {weeks_left} weeks, {months_left} months left."
print(total)
