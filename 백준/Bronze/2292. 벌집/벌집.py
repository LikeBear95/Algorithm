N = int(input())
i = 0
while(N>0):
        if i == 0:
                N -= 1
                i += 1
        else:
                N -= 6 * i
                i += 1

print(i)