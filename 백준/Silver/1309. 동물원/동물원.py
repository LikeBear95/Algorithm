n = int(input())

prev2 = 1
prev1 = 3

if n == 1:
    print(prev1 % 9901)
else:
    for i in range(2, n+1):
        current = (prev2 + prev1*2) % 9901
        prev2 = prev1
        prev1 = current

    print(prev1)
