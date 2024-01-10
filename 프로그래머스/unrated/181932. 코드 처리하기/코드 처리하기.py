def solution(code):
    ret = ''
    mode = False
    for i in range(len(code)):
        if code[i] != "1" and i % 2 == int(mode):
            ret += code[i]
        elif code[i] == "1":
            mode = not(mode)
    if not ret:
        ret = "EMPTY"
    return ret