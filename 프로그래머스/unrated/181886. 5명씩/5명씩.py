def solution(names):
    answer = []
    
    answer += names[::5]
    
    # for i in range(len(names)):
    #     if i % 5 == 0:
    #         answer += names[i]
    
    return answer