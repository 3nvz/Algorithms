# find max
# find min
# convert to tuple so it's order and removes duplicates
# loop through every number from min to max and check if this number is in the tuple
# if not add it to the result

nums = [1, 1]
result = []
tup = set(nums)

localMin = min(tup)
localMax = max(tup)

for i in range(localMin, localMax):
    if i not in tup:
        result.append(i)

print(result)

