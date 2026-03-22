n, m = map(int, input().split())
l = list(map(int, input().split()))
print("OUT" if sum(l)-n < m else "DIMI")