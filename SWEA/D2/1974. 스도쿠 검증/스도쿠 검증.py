# T: 테스트 케이스
T = int(input())
for tc in range(1, T + 1):
    arr = [list(map(int, input().split())) for _ in range(9)]
    answer = 1
    check = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    # 가로 검사
    for i in range(9):
        row = []
        for j in range(9):
            row.append(arr[i][j])
        row.sort()
        # print(row)
        if row != check:
            answer = 0
            # print('error')
            break

    # 세로 검사
    for j in range(9):
        col = []
        for i in range(9):
            col.append(arr[i][j])
        col.sort()
        # print(col)
        if col != check:
            answer = 0
            # print('error')
            break

    # 칸 검사
    for i in range(3):
        for j in range(3):
            cube = []
            for a in range(3):
                for b in range(3):
                    cube.append(arr[i*3+a][j*3+b])
            cube.sort()
            # print(cube)
            if cube != check:
                answer = 0
                # print('error')
                break



    print(f'#{tc} {answer}')
    # for i in range(9):
    #     for j in range(9):
    #         print(arr[i][j], end=" ")
    #     print()
