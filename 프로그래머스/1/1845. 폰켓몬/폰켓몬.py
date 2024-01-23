def solution(nums):
    answer = min(len(list(set(nums))), len(nums)/2)
    return answer