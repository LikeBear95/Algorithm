n = int(input())

for i in range(1, 1000000):
    tmp = 0
    num = i
    while(num != 0):
        tmp = tmp + num % 10
        num //= 10

    if tmp + i == n:
        print(i)
        break

else:
    print(0)