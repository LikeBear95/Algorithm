import sys
input = sys.stdin.readline

s = input().rstrip()

for i in ["social", "history", "language", "literacy"]:
    if i in s:
        print("digital humanities")
        break
for j in ["bigdata", "public", "society"]:
    if j in s:
        print("public bigdata")
        break
