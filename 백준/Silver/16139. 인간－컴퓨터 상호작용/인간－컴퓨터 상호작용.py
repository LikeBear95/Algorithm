import sys
input = sys.stdin.readline

word = input()
for _ in range(int(input())):
    alpha, start, end = input().split()
    print(word[int(start):int(end)+1].count(alpha))
