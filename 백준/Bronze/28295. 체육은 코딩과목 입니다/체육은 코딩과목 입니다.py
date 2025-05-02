l = ["N", "E", "S", "W"]
n = 0

for _ in range(10):
    n += int(input())

print(l[n%4])