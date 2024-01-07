def solution(num, total):
    answer = [(total - sum([y for y in range(num)])) / num + x for x in range(num)]
    return answer