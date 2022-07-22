set1 = {10,20,30,40,50}
set2 = {10,15,20,25,30,35}
#printing set
print("Set1 =",set1)
print("Set2 =",set2)
#adding element to set1
set1.add(45)
print("Set1 after adding 45 =",set1)
#printing set difference
print("Set1 - Set2 =",set1.difference(set2))
#removing a given element fron set1
set1.discard(45)
print("Set1 after removing 45 =",set1)
#printing intersection of two sets
print("Set1 intersection Set2 =",set1.intersection(set2))
#Checking disjoint
print("Set1 and Set2 disjoint? =",set1.isdisjoint(set2))
#checking subset
print("Set1 is subset of Set2? =",set1.issubset(set2))
#removing first element of set
set1.pop()
print("Set1 after removing first element",set1)
#set union
print("Set1 union Set2 =",set1.union(set2))
#printing symmetric difference
print("Symmetric defference =",set1.symmetric_difference(set2))
