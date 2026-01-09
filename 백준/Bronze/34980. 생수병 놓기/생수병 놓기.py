import sys
input = sys.stdin.readline

n = int(input())
a = input().rstrip()
b = input().rstrip()

if a == b:
    print("Good")
elif a.count("w") > b.count("w"):
    print("Oryang")
elif a.count("w") < b.count("w"):
    print("Manners maketh man")
else:
    print("Its fine")