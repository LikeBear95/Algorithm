N = int(input())
i = 1
while(N > i):
        N -= i
        i += 1

if i % 2:
        print(f'{i-N+1}/{N}')
else:
        print(f'{N}/{i-N+1}')