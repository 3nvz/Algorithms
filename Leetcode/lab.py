

startTime = [1,2,3]
endTime = [3,2,7]
queryTime = 4

res = 0

for s, e in zip(startTime, endTime):
    if s <= queryTime <= e:
        res += 1

print(res)
