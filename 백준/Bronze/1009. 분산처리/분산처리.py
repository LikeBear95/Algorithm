l = [[0], [1], [2, 4, 8, 6], [3, 9, 7, 1], [4, 6], [5], [6], [7, 9, 3, 1], [8, 4, 2, 6], [9, 1]]
for _ in range(int(input())):
    a, b = map(int, input().split())
    answer = l[a%10][(b-1)%len(l[a%10])]
    print(answer if answer else 10)