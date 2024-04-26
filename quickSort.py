
# Used first element of arr as pivot which is not optimal, better random or median values - did it for test purposes
def quicksort(arr):
    if len(arr) <= 1:
        return arr    
    else:
        pivot = arr[0]    
        leftPartition = []
        rightPartition = []

        for item in arr[1:]:
            if item < pivot:
                leftPartition.append(item)
            else:
                rightPartition.append(item)
    
        return quicksort(leftPartition) + [pivot] + quicksort(rightPartition)
    


sortMe = [42, 87, 19, 63, 56, 94, 28, 70, 11, 88, 49, 32, 73, 5, 39]
sortedArr = quicksort(sortMe)

print("Unsorted array: ", sortMe)
print("Sorted array: ", sortedArr)



"""
Explanation
1. Get a random pivot point to justify O(nlogn) time complexity
    - In this case for simplicity I still chose the last one
2. Determine low and high of the array 
3. Create 2 pointers: itemLeft and itemRight
4. Starting from left to right
    itemLeft starts at arr[0 - 1]
    itemRight start at arr[0]

    SUDO Code

Move itemRight by +1 
If itemRight < Pivot move itemLeft +1 and swap itemRight with itemLeft
If itemRight > Pivot move itemRight +1, but keep itemLeft where it was
Repeat until itemRight == Pivot then itemLeft +1 and swap pivot with itemLeft
Now pivot is on it's right final position
Repeat these steps with left and right partition of the newly set pivot


"""