import sys
input = sys.stdin.readline

n = int(input())
s = input().rstrip()
t = input().rstrip()

m = len(s)

if n%2:
    for i in range(m):
        if s[i] == t[i]:
            print("Deletion failed")
            break
    else:
        print("Deletion succeeded")

else:
    for i in range(m):
        if s[i] != t[i]:
            print("Deletion failed")
            break
    else:
        print("Deletion succeeded")