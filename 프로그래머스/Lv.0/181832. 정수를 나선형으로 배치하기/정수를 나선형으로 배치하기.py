def solution(n):
    vector = [[0,1], [1,0], [0,-1], [-1,0]]
    vec = 0
    answer = [[0] * n for _ in range(n)]
    i = 0
    j = 0
    for num in range(n**2):
        answer[i][j] = num + 1
        a, b = vector[vec]
        if i+a < 0 or j+b < 0 or i+a >= n or j+b >= n or answer[i+a][j+b] != 0:
            vec += 1
            if vec >= 4:
                vec = 0
            a, b = vector[vec]
        i += a
        j += b
    return answer