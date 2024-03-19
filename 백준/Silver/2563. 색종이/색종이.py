n = int(input())
sqr = [[0]*100 for _ in range(100)]
answer = 0

for i in range(n):
    w, h = map(int, input().split())
    for x in range(10):
        for y in range(10):
            if sqr[x+w][y+h] == 0:
                sqr[x+w][y+h] = 1
                answer += 1

print(answer)