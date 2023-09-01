# T: 테스트 케이스의 개수 입력
T = int(input())

# 각 테스트 케이스를 순회
for t in range(1, T+1):
    # numbers: 입력된 숫자를 문자열로 저장, count: 교환 횟수
    numbers, count = input().split()
    count = int(count)

    # nums: 현재 순열을 저장하는 집합
    nums = set([numbers])

    # SET: 새로운 순열을 저장하는 집합
    SET = set()

    # 주어진 교환 횟수 동안 최대 숫자를 찾음
    for _ in range(count):
        while nums:
            n = nums.pop()
            n = list(n)
            for i in range(len(numbers)):
                for j in range(i + 1, len(numbers)):
                    # 두 자릿수 교환
                    n[i], n[j] = n[j], n[i]
                    SET.add(''.join(n))  # 교환한 순열을 SET에 추가
                    n[i], n[j] = n[j], n[i]  # 다음 순열을 위해 원래대로 돌려놓음
        # nums와 SET을 교체하여 다음 라운드를 위한 순열 준비
        nums, SET = SET, nums

    # nums에서 가장 큰 숫자를 찾아 결과로 출력
    result = max(nums)
    print(f'#{t} {result}')
