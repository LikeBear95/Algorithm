def factorial(number):
    if number == 0:
        return 1
    else:
        return number * factorial(number - 1)

def solution(balls, share):
    answer = factorial(balls) / (factorial(balls - share) * factorial(share))
    return answer