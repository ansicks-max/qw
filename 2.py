'''Question 2: Reverse an array in-place

Problem: Given an array, reverse it without using a new array or built-in reverse functions (no arr[::-1], no .reverse()).

Example:

Input: [1, 2, 3, 4, 5]
Output: [5, 4, 3, 2, 1]'''

from array import array

arr = array("i", [1, 2, 3, 4, 5])
def reverse_array(arr):
    start = 0 
    end = len(arr) - 1

    for i in range(len(arr) // 2):
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1    
print("Original array:", arr)
reverse_array(arr)
print("Reversed array:", arr)
