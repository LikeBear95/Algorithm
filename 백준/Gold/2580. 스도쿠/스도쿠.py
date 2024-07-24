import sys
input = sys.stdin.readline

def dfs(blank):
    if not blank:
        return True
    i, j = blank[0]
    for num in range(1, 10):
        if is_safe(i, j, num):
            sdk[i][j] = num
            if dfs(blank[1:]):
                return True
            sdk[i][j] = 0
    return False

def is_safe(row, col, num):
    for i in range(9):
        if sdk[row][i] == num or sdk[i][col] == num:
            return False
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if sdk[start_row + i][start_col + j] == num:
                return False
    return True


sdk = [list(map(int, input().split())) for _ in range(9)]
blank = [(i, j) for i in range(9) for j in range(9) if sdk[i][j] == 0]

dfs(blank)

for i in range(9):
    print(*sdk[i])
