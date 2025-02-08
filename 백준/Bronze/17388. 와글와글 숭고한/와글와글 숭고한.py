l = list(map(int, input().split()))
s = ['Soongsil', 'Korea', 'Hanyang']
if sum(l) >= 100:
    print("OK")
else:
    print(s[l.index(min(l))])