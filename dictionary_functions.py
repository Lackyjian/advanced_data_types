dict1 = {
  "key1": "abc",
  "key2": 123,
  "key3": "xyz"
}
#printing dictionary
print("Dictionary =",dict1)
#printing dictionary keys
print(dict1.keys())
#printing dictionary values
print(dict1.values())
#printing value from given key
print("Value at key1 =", dict1.get("key1"))
#removing element with given key
dict1.pop("key2")
print("Dictionary after removing value at key2 =",dict1)
#removing last key-value
dict1.popitem()
print("Dictionary after removing last key-value =",dict1)
