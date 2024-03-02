# Python Conditions and If statements
# Python supports the usual logical conditions from mathematics:

# Equals: a == b
# Not Equals: a != b
# Less than: a < b
# Less than or equal to: a <= b
# Greater than: a > b
# Greater than or equal to: a >= b
# These conditions can be used in several ways, most commonly in "if statements" and loops.

# An "if statement" is written by using the if keyword

a=10
b=20
if(b>a):
    print("b is greater than a")
    
    
# Elif
# The elif keyword is Python's way of saying "if the previous conditions were not true, then try this condition".    

num1=90
num2=90

if(num2>num1):
    print("num2 is greater than num1")
elif(num1 == num2):
    print("num1  is equal to num2")    

# Elif
# The elif keyword is Python's way of saying "if the previous conditions were not true, then try this condition".

if a > b: print("a is greater than b")

# Short Hand If ... Else
# If you have only one statement to execute, one for if, and one for else, you can put it all on the same line:


num3 = 5
num4 = 330
print("num1") if a > b else print("num4")

# Example: 01
# Print square root of negative or positive number using if and operators.

# userInput = int(input("Enter a Number : "));
# if(userInput>0):
#     print("The squar root  of positive number is ", userInput ** (1/2))
# elif(userInput<=0):
#     print("Can't calculate the square of negative number is")

# Example: 02
# Write conditional statements to print value of 0 to 1 and 1 to 0 and numbers in between

userInput1 = int(input("Enter a Number to change the value : "))
if(userInput1 == 1):
    userInput1 = 0
    print(userInput1)
if(userInput1 == 0):
    userInput1 = 1
    print(userInput1)
if(userInput1>2 or userInput1<0):
    print("you have entered number between 0 to 1")        
   






















