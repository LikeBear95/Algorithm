n = int(input())
Y = M = 0
lst = list(map(int, input().split()))
for i in lst:
    Y += i//30 + 1
    M += i//60 + 1

Y *= 10
M *= 15

if Y > M:
    print("M", M)
elif Y < M:
    print("Y", Y)
else:
    print("Y M", Y)