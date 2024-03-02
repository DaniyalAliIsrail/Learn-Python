# Python For Loops
# A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string

fruits = ["apple","bannana","cherry"];
for x in fruits: 
 print(x)
 
for x in "banana":
  print(x)
  
# The range() Function
# To loop through a set of code a specified number of times, we can use the range() function:

for x in range(11):
  print(x)
  
  
#The while Loop
# With the while loop we can execute a set of statements as long as a condition is true.

i = 1
while i < 6:
  print(i)
  i += 1

# Example #1
# Print Karachi Pakistan 100 times in a separate line

k=1
while(i<=10):
  print("karachi pakistan")
  i+=1


# The break Statement
# With the break statement we can stop the loop even if the while condition is true:

iterNum1 = 1
while iterNum1 < 6:
  print(iterNum1)
  if( iterNum1 == 3):
    break
  iterNum1 += 1

# Example # 2
# Take collection of number input from user. Print the total positive and negative number

pcount=0
ncount=0
count = int(input("how many number you wants ?"))
j=1
while(j<=count):
  num = int(input("Enter the number : "))
  if(num>0):
    pcount+=1
  else:
    ncount+=1
  j+=1
print("positive",pcount)
print("negative",ncount)    
  
# Example # 3
# Fixed a Letter from a to e and then ask the user to guess that letter until correct letter entered

currentValue = 'c'
userValue = input("Guess a number a to e : ")
while(userValue != currentValue):
  print("incorrect value")
  userValue = input("Guess a number a to e")
print("welcome user")  
  


