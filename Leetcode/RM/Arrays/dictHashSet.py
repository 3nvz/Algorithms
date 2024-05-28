
from collections import Counter

# Dictionaries
# Key value pairs
# The String are the keys here
my_dict = {"apple": 1, "banana": 2, "cherry": 3}
print(my_dict["banana"])  # Output: 2


# Find the key associated with value 2
foundKey = None
for key, value in my_dict.items():
    if value == 2:
        foundKey = key
        break
print(foundKey)


# Counter
# Create dictionaries from lists for example with Counter
elements = ['apple', 'banana', 'apple', 'cherry', 'banana', 'banana']
count = Counter(elements)
print(count)

randomString = "abracadabra"
countedString = Counter(randomString)
print(countedString)


# HashSets
# Unordered collection of unique elements
my_set = {"apple", "banana", "cherry"}
print("banana" in my_set)  # Output: True

