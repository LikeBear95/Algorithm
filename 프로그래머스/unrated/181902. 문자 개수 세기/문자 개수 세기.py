def solution(my_string):
    alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
    lst = [0] * 52
    for s in my_string:
        lst[alpha.index(s)] += 1
    return lst