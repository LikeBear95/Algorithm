n = int(input())
lst = list(map(int, input().split()))
t, p = map(int, input().split())

a = 0
for i in lst:
    a += i//t
    a += 1 if i%t else 0

print(a)
print(n//p, n%p)
