age = int(input("Enter age: "))

if age >= 0 and age <=12:
    print("You're Child")
elif age >= 13 and age <=19:
    print("You're Teenager")
elif age >= 20 and age <=59:
    print("You're Adult")
else:
    print("You're Senior")
# Add your if-elif-else statements here
# 0-12: Child
# 13-19: Teenager  
# 20-59: Adult
# 60+: Senior #age >= 60: