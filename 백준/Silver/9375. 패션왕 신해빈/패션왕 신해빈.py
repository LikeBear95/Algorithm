import sys
input = sys.stdin.readline

for _ in range(int(input())):
    wear = {}
    
    for _ in range(int(input())):
        a, b = input().split()
        wear[b] = wear.get(b, 0) + 1
    
    result = 1
    for i in wear.values():
        result *= (i+1)
    
    print(result-1)