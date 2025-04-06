import sys
input = sys.stdin.readline

wrong = {}
right, count = 0, 0

while True:
    t = input().rstrip()
    if t == "-1":
        break
    time, problem, tf = map(str, t.split())
    if tf == "wrong":
        wrong[problem] = wrong.get(problem, 0) + 1
    else:
        right += wrong.get(problem, 0) * 20 + int(time)
        count += 1
        
print(count, right)