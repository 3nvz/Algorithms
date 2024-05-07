
# O(logn) time complexity
# object to search has to be ordered

searchMe = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
needle = 11

low = 0
high = len(searchMe) - 1

while (low <= high):

    mid = int((low + high)/2)

    if needle == searchMe[mid]:
        print("Needle", needle, "Found at index: ", mid)
        break
    
    if needle < searchMe[mid]:
        high = mid - 1
    
    if needle > searchMe[mid]:
        low = mid + 1


"""
SUDO CODE

mid = searchMe/2 - abs
low = searchMe[0]
high = searchMe[-1]

if needle == mid:
    return needle

if needle < mid:
    high = mid - 1

if needle > mid:
    low = mid + 1

do all these operations while low is smaller than high

"""
