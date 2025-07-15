l = [0, 1.5]

for i in range(2):
    a, b, c, d, e, f = map(int, input().split())
    l[i] += a*13 + b*7 + c*5 + d*3 + e*3 + f*2

print("cocjr0208" if l[0]>l[1] else "ekwoo")
