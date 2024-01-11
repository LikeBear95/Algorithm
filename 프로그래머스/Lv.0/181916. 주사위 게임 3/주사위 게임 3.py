def solution(a, b, c, d):
    dice = [0] * 7
    for num in [a, b, c, d]:
        dice[num] += 1
    if dice.count(4):
        answer = 1111 * dice.index(4)
    elif dice.count(3):
        answer = (10 * dice.index(3) + dice.index(1)) ** 2
    elif dice.count(2) == 2:
        p, q = [x for x in range(7) if dice[x] == 2]
        answer = (p + q) * abs(p - q)
    elif dice.count(2) == 1:
        q, r = [x for x in range(7) if dice[x] == 1]
        answer = q * r
    else:
        answer = min(a, b, c, d)
    return answer