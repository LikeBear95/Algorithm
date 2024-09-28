quardant = {"Q1": 0, "Q2": 0,"Q3": 0,"Q4": 0, "AXIS": 0}

for _ in range(int(input())):
    x, y = map(int, input().split())
    if x == 0 or y == 0:
        quardant["AXIS"] += 1
    elif x > 0 and y > 0:
        quardant["Q1"] += 1
    elif x < 0 and y > 0:
        quardant["Q2"] += 1
    elif x < 0 and y < 0:
        quardant["Q3"] += 1
    elif x > 0 and y < 0:
        quardant["Q4"] += 1

for i in quardant:
    print(f'{i}: {quardant[i]}')