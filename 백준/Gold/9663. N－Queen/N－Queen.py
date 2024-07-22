import sys
input = sys.stdin.readline

def dfs(num):
    global count

    if num == n:
        count += 1
    else:
        for i in range(n):
            chess[num] = i
            if check(num):
                dfs(num+1)

def check(num):
    for i in range(num):
        if chess[num] == chess[i] or num - i == abs(chess[num] - chess[i]):
            return False
    return True

n = int(input())
chess = [0] * n
count = 0

dfs(0)
print(count)
