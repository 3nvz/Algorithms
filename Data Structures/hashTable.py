
# normal sets no key value pairs, but unordered unique values
s = "bBghhjdd"
chars = set(s)

print(chars)


# hash table with key value pairs
s = "bBghhjdd"
hashTable = {}

for char in s:
    if char in hashTable:
        hashTable[char] += 1
    else:
        hashTable[char] = 1

print(hashTable)