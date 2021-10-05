#4

weight = float(input("Please enter your weight in Kilogeram : "))
height = float(input("Please enter your height in Meter : "))

BMI = weight / (height)**2


print("You'r BMI is : " + str(BMI))

if BMI <= 18.5 :
    print(" You are Underweight")
elif (18.5 < BMI <= 24.9)  :
    print(" You are Normal")
elif (25 < BMI <= 29.9)  :
    print(" You are Overweight")
elif (30 < BMI <= 34.9)  :
    print(" You are Obse")
else:
    print(" You are Extremly obese")