for i in range(1, int(input()) + 1):
    tmp = list(map(int, input().split()))
    n, scores = tmp[0], sorted(tmp[1:], reverse=True)
    max_gap = max(scores[j] - scores[j + 1] for j in range(n - 1))
    
    print(f'Class {i}')
    print(f'Max {scores[0]}, Min {scores[-1]}, Largest gap {max_gap}')
