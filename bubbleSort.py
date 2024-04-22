
# O(n^2) time complexity

sortMe = [42, 87, 19, 63, 56, 94, 28, 70, 11, 88, 49, 32, 73, 5, 39]

def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]

for i in range(len(sortMe)):
    for j in range(len(sortMe) - i - 1):
        if sortMe[j] > sortMe[j + 1]:
            swap(sortMe, j, j + 1)

print("Final sorted array", sortMe)


"""
SUDO CODE

loop through array
start index 0

if sortMe[0] > sortMe[0+1]:
    swap sortMe[0] with sortMe[0+1]

Last index will be always the max, so we repeat with sortMe.length - 1

"""