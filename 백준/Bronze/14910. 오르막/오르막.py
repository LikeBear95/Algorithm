l = list(map(int, input().split()))
print("Good" if l == sorted(l) else "Bad")