a, b = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(set(A + B))

print(2*len(C)-(len(A)+len(B)))
