# lambda
# A lambda is small  anonymous function.
#The expression is executed and the result is returend:
x= lambda a: a+10
print(x(5))

# lamda function can take any number of arguments:
x1=lambda a1 , b1 : a1*b1
returnValue = x1(5,5)
print(returnValue)

# print and add the three value using lambda function
addThreeValue = lambda z1 ,z2 , z3 : z1 + z2 + z3
print(addThreeValue(5,5,5))

# NOTE:  python does not have built-in support for Arrays, but python list can be used instead.
