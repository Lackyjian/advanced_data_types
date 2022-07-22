tuple1 = (10,20,35,60,81,90,90)
#printing 
print("Given tuple =",tuple1)
#counting an element in toupple
print("Count of 90s in given tuple =",tuple1.count(90))
#Printing index of given element
print("Index of 60 in given tuple =",tuple1.index(60))
#adding a new element at end of the tuple
list1 = list(tuple1)
list1.append(100)
tuple1 = tuple(list1)
print("Inserting 100 at the last of tupel =",tuple1)
#adding a new element at given index of the tuple
list1 = list(tuple1)
list1.insert(4,45)
tuple1 = tuple(list1)
print("Inserting 45 at the index 4 of tupel =",tuple1)