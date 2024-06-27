# A sawtooth sequence is a sequence of numbers that alternate between increasing and decreasing. In other words, each element is either strictly greater than its neighbouring elements or strictly less than its neighbouring elements.

# examples

# Given an array of integers arr, your task is to count the number of contiguous subarrays that represent a sawtooth sequence of at least two elements.

# Example

# For arr = [9, 8, 7, 6, 5], the output should be solution(arr) = 4.

# Since all the elements are arranged in decreasing order, it won't be possible to form any sawtooth subarrays of length 3 or more. There are 4 possible subarrays containing two elements, so the answer is 4.

# For arr = [10, 10, 10], the output should be solution(arr) = 0.

# Since all of the elements are equal, none of subarrays can be sawtooth, so the answer is 0.

# For arr = [1, 2, 1, 2, 1], the output should be solution(arr) = 10.

# All contiguous subarrays containing at least two elements satisfy the condition of problem. There are 10 possible contiguous subarrays containing at least two elements, so the answer is 10.

def solution(arr):
    counter = 0
    streak = 0
    previous = False
    if len(arr) > 1:
        for i in range(1, len(arr)):
            if arr[i-1] == arr[i]:
                streak = 0
                previous = False
            else:
                current = arr[i] > arr[i-1]
                if(previous != current):
                    streak = streak + 1
                    previous = current
                else:
                    streak = 1
                counter = counter + streak
    return counter