n = int(input())
t = int(input())
l = list(map(int, input().split()))

print("Padaeng_i Cry" if n > sum(l) else "Padaeng_i Happy")