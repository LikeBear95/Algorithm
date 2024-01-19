def solution(d, budget):
    d.sort()
    for i in range(len(d)):
        if sum(d[:i+1]) > budget:
            return len(d[:i])
    return len(d)