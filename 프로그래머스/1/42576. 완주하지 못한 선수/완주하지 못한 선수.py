def solution(participant, completion):
    for c, p in zip(sorted(completion), sorted(participant)):
        # print(c, p)
        if c != p:
            return p
    else:
        return sorted(participant)[-1]
    # return participant[0]