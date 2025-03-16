def clock_num(a, b, c, d):
    return min(int(f"{a}{b}{c}{d}"), int(f"{b}{c}{d}{a}"), int(f"{c}{d}{a}{b}"), int(f"{d}{a}{b}{c}"))

nums = set()
for i in range(1111, 10000):
    tmp = list(map(int, str(i)))
    if 0 in tmp:
        continue
    nums.add(clock_num(*tmp))

nums = sorted(list(nums))
a, b, c, d = map(int, input().split())
num = clock_num(a, b, c, d)

print(nums.index(num)+1)