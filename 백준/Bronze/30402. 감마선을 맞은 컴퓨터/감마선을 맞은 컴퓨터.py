import sys
input = sys.stdin.readline

for _ in range(15):
    l = list(map(str, input().rstrip().split()))
    if "w" in l:
        print("chunbae")
        break
    elif "b" in l:
        print("nabi")
        break
    elif "g" in l:
        print("yeongcheol")
        break
    