# Write a program that calculates the user’s body mass index (BMI) and classify it as underweight,
# normal, overweight, or obese, based on the table from the United States Centers for Disease Control.
# Bmi = (weight | height*height)
# <=18.4 = underweight
# 18.4 and 24.9 Normal
#25.0 to 39.9 overweight
#>=40.0 obses

userWeight = float(input("Enter a Body Weight in kilogram: "))
userHeight = float(input("Enter a Body Height in Meter: "))

bmi = (userWeight / userHeight*userHeight)

if( bmi < 18.4):
    print("your body weight are underWight")
elif(bmi >= 18.4 or bmi <= 24.9):
    print("your body  weight are normal")
elif(bmi >= 25.0 or bmi <= 39.9):
    print("you body are underweight")
elif(bmi >= 40):
    print("your body weight are obses")            
    