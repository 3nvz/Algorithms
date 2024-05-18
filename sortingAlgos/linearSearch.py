#Linear search (boring) O(n) Complexity

searchMe = [4, 6, 3, 7, 8, 1, 8, 9, 4, 2, 7]
needle = 7
result = []

for i in range(len(searchMe)):
    if needle == searchMe[i]:
        result.append(i)

print("Needle was found on following indexes: ", ', '.join(map(str, result)))