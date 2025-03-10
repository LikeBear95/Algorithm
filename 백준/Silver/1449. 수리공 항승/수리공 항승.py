n, l = map(int, input().split())
hole = sorted(list(map(int, input().split())))
tape = []
count = 0

for i in hole:
    if i not in tape:
        count += 1
        for j in range(i, i+l):
            tape.append(j)

print(count)