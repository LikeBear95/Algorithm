import sys
input = sys.stdin.readline

for _ in range(int(input())):
    s = input().rstrip()
    n = len(s)//2
    print("Do-it" if s[n-1]==s[n] else "Do-it-Not")