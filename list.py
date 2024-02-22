#LIST:
fruits = ['apple','orange','pear','banana']
print(fruits);# print("Access the Apple",fruits[0])

#CONCATENATION:
otherFruits = ["kiwi","strawberry"]
concatFruits = fruits+otherFruits
print("concatenation of fruits & otherFruits",concatFruits)

#NEGATIVE -INDEXING FROM THE BACK OF THE LIST:
print(fruits[-1]) # -1 access the last element of the list

#SLICE OPERATOR:
print("Access apple,orange",fruits[0:2])
print("Access apple,orange,pear",fruits[0:3])
print("Acess apple to length of list",fruits[0:])

#2D LIST
twoDList= [
    ['a','b','c'],
    [1,2,3],
    ['one','two','three']
]
print(twoDList)
#Access the the c letter
print(twoDList[0][2])
#push d on the list
# print(twoDList[0][2].pop())