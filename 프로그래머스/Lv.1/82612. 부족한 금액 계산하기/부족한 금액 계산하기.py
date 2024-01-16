def solution(price, money, count):
    answer = money - (price * sum([x for x in range(1, count + 1)]))
    if answer < 0:
        return -answer
    else:
        return 0