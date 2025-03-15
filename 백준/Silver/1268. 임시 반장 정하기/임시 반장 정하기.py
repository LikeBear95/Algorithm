n = int(input())
students = [list(map(int, input().split())) for _ in range(n)]
count = [0] * n

for i in range(n):
    for j in range(i + 1, n):
        if any(students[i][x] == students[j][x] for x in range(5)):
            count[i] += 1
            count[j] += 1

max_count = max(count)
print(count.index(max_count)+1)
