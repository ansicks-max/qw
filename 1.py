'''Problem: Given an array of integers, find the maximum and minimum elements in a single pass.'''

from array import array


def find_min_max(arr):
    largest = arr[0]
    smallest = arr[0]

    for i in range(1, len(arr)):
        if arr[i] > largest:
            largest = arr[i]
        elif arr[i] < smallest:
            smallest = arr[i]

    print("Largest number in the array is:", largest)
    print("Smallest number in the array is:", smallest)


arr = array("i", [3, 7, 1, 9, 4])

find_min_max(arr)