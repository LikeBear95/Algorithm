import sys
input = sys.stdin.readline

def bt(num, now):
    global count

    if now > num:
        return
    elif now == num:
        count += 1
    else:
        for i in [1, 2, 3]:
            now += i
            bt(num, now)
            now -= i

for _ in range(int(input())):
    count = 0
    bt(int(input()), 0)
    print(count)
