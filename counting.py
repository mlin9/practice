### Return 1 if permutation, else return 0

def solution(A):
    total = 0
    B = [0] * (len(A) + 1)
    for N in A:
        total = total + N
        if N > len(A) or B[N] > 1:
            return 0
        else:
            B[N] = B[N] + 1
    if total != int(len(A) * (len(A) + 1) / 2):
        return 0
    else:
        for i in range(1, len(B)):
            if B[i] != 1:
                return 0
    return 1
    pass

### Return an N-length frequency array that flattens when A[i] == N + 1

def solution(N, A):
    counters = [0] * N
    maximum = 0
    maxxed = False
    for i in A:
        if 0 < i and N >= i:
            counters[i - 1] = counters[i - 1] + 1
            maxxed = False
            if maximum < counters[i - 1]:
                maximum = counters[i - 1]
        elif N < i and not maxxed:
            counters = [maximum] * N
            maxxed = True
    return counters
    pass
