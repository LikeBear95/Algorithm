def solution(polynomial):
    poly = list(map(str, polynomial.split()))
    tmp = [0, 0]
    for p in poly:
        if 'x' in p:
            if p == 'x':
                tmp[0] += 1
            else:
                tmp[0] += int(p[:-1])
        elif p.isdigit():
            tmp[1] += int(p)
    
    if tmp[0] == 0 and tmp[1] == 0:
        answer = ''
    elif tmp[0] == 0:
        answer = f'{tmp[1]}'
    elif tmp[1] == 0:
        if tmp[0] == 1:
            answer = 'x'
        else:
            answer = f'{tmp[0]}x'
    else:
        if tmp[0] == 1:
            answer = f'x + {tmp[1]}'
        else:
            answer = f'{tmp[0]}x + {tmp[1]}'
    return answer