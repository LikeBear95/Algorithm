def solution(A, B):
    for s in range(len(A)-1, 0, -1):
        if A[s:] + A[:s] == B:
            answer = len(A) - s
            break
        else:
            answer = -1
    if A == B: answer = 0
    return answer