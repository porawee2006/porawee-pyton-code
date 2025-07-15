weight = float(input("enter your weight(kilograms):"))
height = float(input("enter your height(meters):"))
BMI = weight / height**2
if BMI < 18.5:
    print("Underweight")
if BMI >= 18.5 and BMI <=24.9:
    print("Normal weight")
if BMI >= 25.0 and BMI <=29.9:
    print("Overweight")
if BMI <= 30:
    print("Obese")