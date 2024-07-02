### Cycle the elements K times.
def solution(A, K):
    if len(A) > 1:
        for _ in range(K):
            A.insert(0, A.pop())
    return A
    pass

### Find integer of odd frequency.

# Hashmap implementation.
# Optimal solution
def solution(A):
    hashmap = {}
    result = 0
    for element in A:
        if element not in hashmap:
            hashmap[element] = True
            result = result + element
        else:
            del hashmap[element]
            result = result - element
    return result
    pass

# Frequency array implementation.
# Fails performance tests
def solution(A):
    result = 0
    freq = []
    for number in A:
        if number not in freq:
            result = result + number
            freq.append(number)
        else:
            result = result - number
            freq.remove(number)
    return result
    pass

# Nested loop implementation for space complexity.
def solution(A):
    while len(A) > 1:
        for i in range(1, len(A)):
            if A[0] == A[i]:
                A.pop(i)
                A.pop(0)
                break
    return A[0]
    pass

### Find minimum absolute difference.
import sys

def abs(x):
    if x < 0:
        return x * -1
    return x

def sum(A):
    total = 0
    for N in A:
        total += N
    return total

def solution(A):
    subtotal = 0
    minimum = sys.maxsize
    total = sum(A)
    for i in range(0, len(A) - 1):
        subtotal = subtotal + A[i]
        difference = abs(2 * subtotal - total)
        if minimum > difference:
            minimum = difference
    return minimum
    pass