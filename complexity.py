import math

def solution(X, Y, D):
    # Implement your solution here
    if(Y > X):
        return math.ceil((Y - X)/D)
    else:
        return 0
    pass