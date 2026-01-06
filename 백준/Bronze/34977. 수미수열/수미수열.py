n = int(input())
l = list(map(int, input().split()))

for i in range(1, n//2+1):
    if l[:i] == l[-i:]:
        print("yes")
        break
else:
    print("no")