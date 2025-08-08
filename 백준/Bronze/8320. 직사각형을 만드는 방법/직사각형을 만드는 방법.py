n = int(input())
c = 0

for i in range(1, int(n**0.5)+1):
    j = n // i
    c += j - i +1

print(c)