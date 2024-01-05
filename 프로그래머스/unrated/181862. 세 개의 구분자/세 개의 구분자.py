def solution(myStr):
    answer = list(map(str, myStr.replace("a", " ").replace("b", " ").replace("c", " ").split()))
    if not answer:
        answer = ["EMPTY"]
    return answer