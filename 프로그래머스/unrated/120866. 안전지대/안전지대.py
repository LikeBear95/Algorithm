def solution(board):
    n = len(board)
    answer = n * n
    is_danger = [(0, 0), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]
    for i in range(n):
        for j in range(n):
            for k in is_danger:
                a, b = k
                if i + a >= 0 and i + a < n and j + b >= 0 and j + b < n and board[i+a][j+b] == 1:
                    answer -= 1
                    break
    # answer = MAP.count(1)
    return answer