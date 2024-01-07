def solution(arr):
    answer = 0
    change = 0
    for num in arr:
        while(1):
            tmp = num
            if num >= 50 and not(num % 2):
                num /= 2
                change += 1
            elif num < 50 and num % 2:
                num = num * 2 + 1
                change += 1
            else:
                answer = max(answer, change)
                change = 0
                break
    return answer