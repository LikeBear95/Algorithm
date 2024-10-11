for _ in range(int(input())):
    k = int(input())
    n = int(input())
    floor = [[0]*n for _ in range(k+1)]
    floor[0] = [x+1 for x in range(n)]
    for i in range(1, k+1):
        for j in range(n):
            if j == 0:
                floor[i][j] = floor[0][0]
            else:
                floor[i][j] = floor[i-1][j] + floor[i][j-1]
    print(floor[k][n-1])