# Q1:python program to swap 4 variable values(input four values sample input)
def swapVar(num1, num2, num3, num4):
    print("a =", num1, ", b =", num2, ", c =", num3, ", d2 =", num4)
    num1, num2, num3, num4 =  num4, num3, num2, num1 
    print("a =", num1, ", b =", num2, ", c =", num3, ", d2 =", num4)

#input from user
num1 = int(input("Enter the value of num1: "))
num2 = int(input("Enter the value of num2: "))
num3 = int(input("Enter the value of num3: "))
num4 = int(input("Enter the value of num4: "))

# Calling the function to swap variables
swapVar(num1, num2, num3, num4)

