n = int(input())
lst = [0, 1, 3]

for i in range(3, n+1):
    lst.append((lst[i-2]*2+lst[i-1])%10007)

print(lst[n])