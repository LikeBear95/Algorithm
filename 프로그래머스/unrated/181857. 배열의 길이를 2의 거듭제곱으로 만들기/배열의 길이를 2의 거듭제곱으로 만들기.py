def solution(arr):
    two = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]
    for num in two:
        if len(arr) <= num:
            arr += [0] * (num - len(arr))
            break
    answer = arr
    return answer