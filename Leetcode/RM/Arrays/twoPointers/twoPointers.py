
# Brute force two pointers
# k starts from i
numOfKIterations = 0

for i in range(5):
    print("i: ", i)
    for k in range(i, 5):
        numOfKIterations += 1
        print("k: ", k)
    print("Number of k iterations: ", numOfKIterations)
    numOfKIterations = 0


# Chase Pointers
# First pointer runs faster than the second one
# Both start at the same index
# Example: First pointer jumps 2 indexes, second pointer only one
target = 5
fastFirst = 0
slowSecond = 0

while fastFirst <= target:
    print("Slow Index: ", slowSecond, " Fast Index: ", fastFirst)
    fastFirst += 2
    slowSecond += 1


# Start and End Pointers
# One pointer starts in the beginning of the list, the otehr one at the end
# Eventually they meet in the middle
start = 0
end = 6

while start <= end:
    print("Start: ", start, " End: ", end)
    start += 1
    end -= 1
    if start == end:
        print("Middle was met at: ", start)


# Slidin Window
# Initialize summing first k elements
# Slide the window from left to right adding the next element on the right and removing the one on the left (first element)
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
k = 3
arrLength = len(arr)

winSum = sum(arr[:k])
winMax = winSum

for i in range(arrLength - k):
    winSum = winSum - arr[i] + arr[i + k]
    winMax = max(winMax, winSum)

print("Window max is: ", winMax)





