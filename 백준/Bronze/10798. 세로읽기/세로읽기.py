answer = ''
lst = [input() for _ in range(5)]

for i in range(15):
    for j in range(5):
        try:
            answer += lst[j][i]
        except:
            continue

print(answer)
