# Exercise: Lists 
# (i)Play with some of the list functions. You can find the methods you can call on an object via the dir

# append: This method adds an element to the end of the list.
lst = ["nodejs","reactjs","expressjs"]
lst.append("mongodb")
print(lst)

# extend: This method extends the list by appending elements from the iterabl
lst1 = ["nodejs","reactjs","expressjs"]
lst2 = ["c","c#",".net"]
lst1.extend(lst2)
print(lst2)

# insert: This method inserts an element at a specified index.
lst3 =  ["nodejs","reactjs","expressjs"]
lst3.insert(1,"angular")
print(lst3)

# remove: This method removes the first occurrence of a value from the list.
lst4 =  ["nodejs","reactjs","expressjs"]
lst4.remove("reactjs")
print(lst4)

# pop: This method removes and returns the element at the specified index. If no index is specified, it removes and returns the last element.
lst5 =  ["nodejs","reactjs","expressjs"]
lstAll = lst5.pop()
print(lst5)

# index: This method returns the index of the first occurrence of a value in the list.
lst6 = ["nodejs","reactjs","expressjs"]
lstAll1 = lst6.index('reactjs')
print(lstAll1)

# Python List reverse()
lst7 = ["nodejs","reactjs","expressjs"]
lst7.reverse()
print(lst7)

#(ii)Write a Python program to count the number of strings where the string length is 2 or more and the  first and last character are same from a given list of strings. 
# Sample List : ['abc', 'xyz', 'aba', '1221']
# Expected Result : 2. 

sample_list = ['abc', 'xyz', 'aba', '1221']
counter = 0
for string in sample_list:
    if len(string) >= 2 and string[0] == string[-1]:
     counter += 1
    
print("first and last letter are same in this list item is",counter)

# Exercise: List Comprehensions 
# (i)Write a list comprehension which, from a list, generates a lowercased version of each string that has 
# length greater than five. 

original_list = ['Gava', 'Banana', 'Orange', 'Grape', 'Strawberry', 'Watermelon', 'Pineapple']
for item in original_list:
    if len(item) >= 5:
        print(item.lower())
    else:
        print(item) 
        
# (ii)Write a Python program to print a specified list after removing the 0th, 4th and 5th elements 
# Sample List : ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
# Expected Output : ['Green', 'White', 'Black']

colors = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow', 'Teapink']
positions_to_remove = [0, 4, 5]
# Create a new list without the colors we want to remove
new_list = []
for index,colors in enumerate(colors):
    print(index,colors)
    if index not in positions_to_remove:
            new_list.append(colors) 
print(new_list)                   