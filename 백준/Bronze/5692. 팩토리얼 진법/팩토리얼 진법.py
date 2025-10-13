import sys
input = sys.stdin.readline

while True:
    n = input().rstrip()
    if n == '0':
        break
    n = "0"*(5-len(n)) + n
    print(int(n[0])*120 + int(n[1])*24 + int(n[2])*6 + int(n[3])*2 + int(n[4]))