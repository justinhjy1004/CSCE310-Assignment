import math
import random

# Partitions the given array around a pivot element
# which is chosen to be the last element.
# Returns the index at which the pivot element ends up
def partition(arr):
    if len(arr) == 1:
        return 0
    i = -1
    n = len(arr)-1
    pivot = arr[n]

    for j in range(0 , n):
        if arr[j] <= pivot:
            i = i+1
            arr[i],arr[j] = arr[j],arr[i]

    arr[i+1],arr[n] = arr[n],arr[i+1]

    return ( i+1 )

# Recursive algorithm that calls partition until median is found
def find_median(array, og_length, adj_index=0):
    # calls partition, gets the index of the last array in order
    m = partition(array)

    # handles the corner case of length of array = 1
    if len(array) == 1:
        return array[m]

    # base case, returns the value of the index when the
    # middle index of the"sorted" array is found
    if m + adj_index == math.floor(og_length/2):
        return(array[m])

    # if the index of the sorted value is bigger than the median
    # find median at the left half of the array
    if m + adj_index > math.floor(og_length/2):
        return find_median(array[:m], og_length, adj_index)
    # find the median at the right half of the array
    else:
        adj_index = adj_index + m # adjust the index to keep track of the "actual" index
        return find_median(array[m:], og_length, adj_index)


if __name__ == "__main__":

    array = []
    for i in range(500):
        array.append(random.randint(0,1000))

    print(len(array))
    print(array)
    print(sorted(array)[math.floor(len(array)/2)])
    print(find_median(array, len(array)))
