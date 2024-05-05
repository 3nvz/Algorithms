# O(nlogn) time complexity


def mergeSort(array):

    if len(array) > 1:
        #divide into left and right sections
        m = len(array)//2
        L = array[:m]
        R = array[m:]

        mergeSort(L)
        mergeSort(R)

        i = k = j = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                array[k] = L[i]
                i += 1
            else:
                array[k] = R[j]
                j += 1
            k += 1
    
        #case running out of elements
        while i < len(L):
            array[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            array[k] = R[j]
            j += 1
            k += 1



sortMe = [42, 87, 19, 63, 56, 94, 28, 70, 11, 88, 49, 32, 73, 5, 39]
mergeSort(sortMe)

print(sortMe)