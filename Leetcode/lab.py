# find max
# find min
# convert to tuple so it's order and removes duplicates
# loop through every number from min to max and check if this number is in the tuple
# if not add it to the resultc

from typing import Counter


nums = [4,3,2,7,8,2,3,1]
result = []
tup = set(nums)

d = Counter(nums)
print(d, "Couneter")

localMin = min(tup)
localMax = max(tup)

for i in range(localMin, localMax):
    if i not in tup:
        result.append(i)

print(result)

