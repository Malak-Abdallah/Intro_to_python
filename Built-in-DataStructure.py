# List contains items separated by commas and enclosed within square brackets ([])
# a feature in lists that all the items belonging to a list can be of
# different data type.

list = ['malak', 20, True, 15.5]
print(list[1:3])

list2 = ["hello", "world"]
print("We can concatenate two lists and get the following result: " , list + list2)


list[0]= "Ahmad"
print("we can change the list's elements values and size:")
print(list)

# we can append lists :
list2.append("this is the appended element")
print(list2)
# or more than one element can be added to the list at once using extend():
list.extend([2,5,4])
print("the new list after being extended it:",list)

# we can remove elements as well:
list.remove("Ahmad")
print("the list after removing an element(Ahmad): ",list)

print("the size of the list = ", len(list))

# ----------------------------------
# Tuples:Tuple consists of a number of values separated by commas. Unlike lists, however, tuples are enclosed
# within parentheses and can't change it's elements values and size as lists.

tuple = {'malak', 20, True, 15.5}
tuple2 = {'ahmad', 20, False, 15.5}
print("this is a tuple:",tuple2)
