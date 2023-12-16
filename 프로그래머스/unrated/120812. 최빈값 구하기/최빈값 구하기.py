def solution(array):
    cnt = {}
    
    for num in array:
        if num in cnt:
            cnt[num] += 1
        else:
            cnt[num] = 1
            
    max_cnt = []
    max_values = max(cnt.values())
    
    for num in cnt:
        if cnt[num] == max_values:
            max_cnt.append(num)
    
    if len(max_cnt) > 1:
        answer = -1
    else:
        answer = max_cnt[0]
    return answer