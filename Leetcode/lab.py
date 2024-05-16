
# count up to n + 1
# convert every count starting from 0 to binary
# count the number of 1's in the binary result
# append the number of 1's to the result array

n = 5
result = []
result.append(0)


for i in range(n + 1):
    tmp = bin(i)
    counter = 0
    for char in tmp:
        if char == '1':
            counter += 1
    if counter != 0:
        result.append(counter)

print(result)