# best ccase is O(n) if one value per bucket, worst case if all elements are placed in 1 bucket again because they are so close O(n^2) to O(nlogn)

sortMe = [.42, .32, .33, .52, .37, .47, .51]

def bucketsort(arr):
    bucket = []

    for i in range(len(sortMe)):
        bucket.append([])

    for item in sortMe:
        index = int(10 * item)
        bucket[index].append(item)

    for i in range(len(bucket)):
        bucket[i] = sorted(bucket[i])

    merge = 0
    for i in range(len(arr)):
        for j in range(len(bucket[i])):
            sortMe[merge] = bucket[i][j]
            merge += 1
    
    return arr

sortedArr = bucketsort(sortMe)
print("Soted final array: ", sortedArr)

"""

1. Let's imgaine we want to sort an array
2. The elements of the array will be divided into multiple buckets
3. Number of buckets is equal to the number of elements of array
4. Each buckets is being sorted recursively with the same bucketSort or any other sort

-> If the elements in the array are floats, we can multiple by 10 and take the floor value to assign to a bucket

SUDO CODE

Create a bucket array or map
for i in length sortme
    append i to bucket array

for item in sortme
    index = item * 10
    append item to bucket[index]

sort every bucket
for item in length of bucket
    bucket[item] = sort bucket[item]

get the sorted final array
for i in length of array
    for j in length of bucket[i]
        arr[firstIndex] = bucket[i][j]
    firstIndex + 1

"""