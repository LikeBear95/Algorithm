def find_set(x):
    if relation[x] == x:
        return x

    # return find_set(parent[x])

    # 경로 압축
    relation[x] = find_set(relation[x])
    return relation[x]

# union
def union(x, y):
    # 1. 이미 같은 집합인지 체크
    x = find_set(x)
    y = find_set(y)

    # 대표자가 같으니, 같은 집합이다.
    if x == y:
        # print("싸이클 발생")
        return

    # 2. 다른 집합이라면, 같은 대표자로 수정
    if x < y:
        relation[y] = x
    else:
        relation[x] = y

T = int(input())
for tc in range(1, T + 1):
    # N: 사람수, M: 관계수
    N, M = map(int, input().split())
    relation = [i for i in range(N + 1)]
    for i in range(M):
        a, b = map(int, input().split())
        union(a, b)

    answer = 0
    for j in range(N + 1):
        if j == relation[j]:
            answer += 1

    print(f'#{tc} {answer - 1}')