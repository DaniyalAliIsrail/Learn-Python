# A set is a collection which is unordered, unchangeable*, and unindexed
thisset = {"apple", "banana", "cherry"}
print(thisset)

# Duplicates Not Allowed
# Sets cannot have two items with the same value.
thisset = {"apple", "banana", "cherry", "apple"}
print("Duplicate values are not allowed",thisset)

# The values True and 1 are considered the same value in sets, and are treated as duplicates:
thisset1 = {"apple", "banana", "cherry", True, 1, 2}
print(thisset1)

# The values False and 0 are considered the same value in sets, and are treated as duplicates:
thisset = {"apple", "banana", "cherry", False, True, 0}
print(thisset)

# ACCESS ITEMS:

#CHECK IF IS banana PRESENT IN THE SET: RETURN IS "TRUE" OTHER WISE "FALSE"
checkItem = {"apple", "banana", "cherry"}
print("banana" in checkItem) #return true

#ADD ITEMS
# To add one item to a set use the add() method.
additemSet = {"apple", "banana", "cherry"}
additemSet.add("orange")
print(additemSet)

# Add Sets
# To add items from another set into the current set, use the update() method.

oldSet = {"apple", "banana", "cherry"}
newSet = {"pineapple", "mango", "papaya"}
oldSet.update(newSet)
print("update set",oldSet)

# Remove Item
# To remove an item in a set, use the remove(), or the discard() method.

removeSet = {"apple", "banana", "cherry"}
removeSet.remove("banana")
print(removeSet)

# Note: If the item to remove does not exist, discard() will NOT raise an error.

removeSetDiscard = {"apple", "cherry"}
removeSetDiscard.discard("banana")
print(removeSetDiscard)

#DELETE

# The del keyword will delete the set completely:
delSet = {"apple", "banana", "cherry"}
delSet.clear()
print(delSet)