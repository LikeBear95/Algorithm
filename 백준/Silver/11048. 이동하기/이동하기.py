x, y = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(x)]
new_lst = [[0]*y for _ in range(x)]

new_lst[0][0] = lst[0][0]

for i in range(1, x):
    new_lst[i][0] = lst[i][0] + new_lst[i-1][0]

for j in range(1, y):
    new_lst[0][j] = lst[0][j] + new_lst[0][j-1]

for i in range(1, x):
    for j in range(1, y):
        new_lst[i][j] = lst[i][j] + max(new_lst[i-1][j], new_lst[i][j-1])

print(new_lst[x-1][y-1])