n = int(input())

o = (' *' * n)[:n]
e = ('* ' * n)[:n]

for i in range(n * 2):
    print(o if i % 2 else e)