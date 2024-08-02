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

### Return the local minima bounded by arrays P and Q

# Naive implementation
mapper = { "A": 1, "C": 2, "G": 3, "T": 4}

def solution(S, P, Q):
    M = len(P)
    R = []
    for i in range(M):
        minimum = 4
        for j in range(P[i], Q[i] + 1):
            value = mapper[S[j]]
            if value == 1:
                minimum = 1
                break
            elif mapper[S[j]] < minimum:
                minimum = mapper[S[j]]
        R.append(minimum)
    return R
    pass

# Dynamic implementation
acgt = { "A": 0, "C": 1, "G": 2, "T": 3 }

def solution(S, P, Q):
    counts = [0] * 4
    totals = [[0] * 4]
    result = []
    for k in range(1, len(S) + 1):
        counts[acgt[S[k - 1]]] = counts[acgt[S[k - 1]]] + 1
        totals.append(counts.copy())    
    for i in range(len(P)):
        if Q[i] > P[i]:
            for j in range(4):
                if totals[Q[i] + 1][j] - totals[P[i]][j] != 0:
                    result.append(j + 1)
                    break
        else:
            result.append(acgt[S[P[i]]] + 1)
    return result