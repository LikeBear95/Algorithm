f = [0, 500] + [300] * 2 + [200] * 3 + [50] * 4 + [30] * 5 +  [10] * 6 + [0] * (100-5-4-3-2-1)
s = [0, 512] + [256] * 2 + [128] * 4 + [64] * 8 + [32] * 16 + [0] * (64-16-8-4-2-1)

for _ in range(int(input())):
    a, b = map(int, input().split())
    print((f[a] + s[b])*10000)