list1 = [10,15,16,17,17,90,90]
#Printing list
print("List =",list1)
#Adding element at end of list
list1.append(30)
print("List after appending 30 =",list1)
#Adding element at given index of list
list1.insert(3,60)
print("List after adding element at index 3 =",list1)
#sorting
list1.sort()
print("List after sorting =",list1)
#deleting an element at given index
list1.pop(3)
print("List after deleting element at index 3 =",list1)
#reversing the list
list1.reverse()
print("List after reversing =",list1)
#deleting element with given value
list1.remove(15)
print("List after deleting 15 =",list1)
#Printing the index of given element
print("index of 60 =",list1.index(60))
#counting an element in list
print("count of 90s in list =",list1.count(90))
#clearing all elements from list
list1.clear()
print("List after clearing all elements =",list1)