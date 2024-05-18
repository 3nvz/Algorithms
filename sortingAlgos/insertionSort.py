#O(n) time complexity, worst O(n^2)

def insertionSort(arr):
    
    if len(arr) <= 1:
        return
    
    for i in range(1, len(arr)):
        key = arr[i]
        lastSortedElement = i - 1

        while lastSortedElement >= 0 and key < arr[lastSortedElement]:
            arr[lastSortedElement + 1] = arr[lastSortedElement]
            lastSortedElement -= 1

        # After loop exists this is the position right after the smallest element now - so key is placed right after the smallest position
        arr[lastSortedElement + 1] = key



sortMe = [42, 87, 19, 63, 56, 94, 28, 70, 11, 88, 49, 32, 73, 5, 39]
insertionSort(sortMe)

print(sortMe)