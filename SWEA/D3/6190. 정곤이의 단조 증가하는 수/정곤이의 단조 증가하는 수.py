# T: 테스트 케이스
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    A = list(map(int, input().split()))
    answer = -1

    for i in range(len(A)-1):
        for j in range(i + 1, len(A)):
            temp = A[i] * A[j]
            str_temp = str(temp)
            if answer < temp and temp >= 10:
                for k in range(len(str_temp) - 1):
                    if str_temp[k] > str_temp[k + 1]:
                        break
                else:
                    answer = temp
            elif answer < temp:
                answer = temp

    print(f'#{tc} {answer}')
