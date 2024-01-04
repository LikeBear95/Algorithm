def solution(dots):
    answer = 0
    line = set()
    tmp = []
    for a in range(len(dots)):
        for b in range(a + 1, len(dots)):
            if dots[a][1]-dots[b][1] == 0:
                line.add(1)
                tmp.append(1)
            else:
                line.add((dots[a][0]-dots[b][0])/(dots[a][1]-dots[b][1]))
                tmp.append((dots[a][0]-dots[b][0])/(dots[a][1]-dots[b][1]))
    if tmp[0] == tmp[5] or tmp[1] == tmp[4] or tmp[2] == tmp[3]:
        answer = 1
    return answer