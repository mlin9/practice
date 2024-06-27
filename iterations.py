# Naive Implementation with Arrays

def abs(x):
    if x < 0:
        return x * -1
    return x

def pow(x, y):
    result = 1
    for i in range(0, abs(y)):
        result = result * x
    if y < 0:
        return 1/result
    return result

def binary(x):
    result = []
    definite = False
    for i in range(32, -1, -1):
        if x - pow(2, i) >= 0:
            x = x - pow(2, i)
            result.append(1)
            definite = True
        elif definite:
            result.append(0)
    return result

def gap(x):
    result = 0
    arr = binary(x)
    indices = []
    for i in range(0, len(arr)):
        if arr[i] == 1:
            indices.append(i)
    for j in range(0, len(indices) - 1):
        distance = indices[j+1] - indices[j] - 1
        if result < distance:
            result = distance
    return result


def solution(N):
    return gap(N)

# Decimal Implementation

def solution(N):
    temp_count = 0
    max_gap = 0
    for i in reversed(range(22)):
        if(0 <= N - 2**i):
            for j in reversed(range(i + 1)):
                if 0 > N - 2**j:
                  temp_count = temp_count + 1
                elif 0 <= N - 2**j:
                    if(temp_count > max_gap):
                        max_gap = temp_count
                    N = N - 2**j
                    temp_count = 0
            break
    return max_gap