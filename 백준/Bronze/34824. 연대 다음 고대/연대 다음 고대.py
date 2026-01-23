import sys
input = sys.stdin.readline

k = 0
y = 0

for i in range(int(input())):
    if k and y:
        break
    t = input().rstrip()
    if t == "korea":
        k = i+1
    elif t == "yonsei":
        y = i+1

print("Yonsei Won!" if k>y else "Yonsei Lost...")