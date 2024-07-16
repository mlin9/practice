### Return the prefix sum of the total array.

def solution(A):
    N = len(A)
    P = [0] * (N + 1)
    for k in range(1, N + 1):
        P[k] = P[k - 1] + A[k - 1]
    return P[N] + P[N - 1]
    pass

### Return the count of all combinations A[i] = 0 and A[j] = 1, i < j

def solution(A):
    zeroes = 0
    pairs = 0
    for N in A:
        pairs = pairs + zeroes * N
        if pairs > 1000000000:
            return -1
        elif N == 0:
            zeroes = zeroes + 1
    return pairs
    pass