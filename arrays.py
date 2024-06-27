def solution(A, K):
    if len(A) > 1:
        for _ in range(K):
            A.insert(0, A.pop())
    return A
    pass

def solution(A):
    # Implement your solution here
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
