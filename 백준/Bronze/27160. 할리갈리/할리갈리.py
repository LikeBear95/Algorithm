d = {"STRAWBERRY":0, "BANANA":0, "LIME":0, "PLUM":0}
for _ in range(int(input())):
    s, t = map(str, input().split())
    d[s] += int(t)
print("YES" if 5 in d.values() else "NO")