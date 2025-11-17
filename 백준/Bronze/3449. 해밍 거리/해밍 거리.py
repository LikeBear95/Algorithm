import sys
input = sys.stdin.readline

for _ in range(int(input())):
    a = input().rstrip()
    b = input().rstrip()
    c = 0
    
    for i in range(len(a)):
        c += 1 if a[i] != b[i] else 0
    print(f'Hamming distance is {c}.')