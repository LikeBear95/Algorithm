di = [1, 0, -1, 0]
dj = [0, 1, 0, -1]

def dfs(r, c, word):
    if len(word) == 7:
        num_set.add(word)
        return

    for k in range(4):
        ni, nj = r + di[k], c + dj[k]
        if 0 <= ni < 4 and 0 <= nj < 4:
            dfs(ni, nj, word + arr[r][c])


T = int(input())
for tc in range(1, T + 1):
    arr = [list(map(str, input().split())) for _ in range(4)]

    num_set = set()

    for i in range(4):
        for j in range(4):
            dfs(i, j, '')
            pass

    answer = len(num_set)

    print(f'#{tc} {answer}')
