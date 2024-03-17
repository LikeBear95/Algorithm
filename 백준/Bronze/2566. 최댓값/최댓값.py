answer = [0, 1, 1]
lst = [list(map(int, input().split())) for _ in range(9)]

for i in range(9):
    for j in range(9):
        if lst[i][j] > answer[0]:
            answer[0] = lst[i][j]
            answer[1] = i + 1
            answer[2] = j + 1

print(answer[0])
print(answer[1], answer[2])
