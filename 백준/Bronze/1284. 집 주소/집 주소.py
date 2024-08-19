while True:
    n = input()
    answer = len(n) + 1
    if n == "0":
        break
    for i in n:
        if i == "1":
            answer += 2
        elif i == "0":
            answer += 4
        else:
            answer += 3
    print(answer)
