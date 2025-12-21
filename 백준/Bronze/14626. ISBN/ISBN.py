t = input()
n, m = 0, 0

for i in range(len(t)):
    if t[i].isdigit():
        n += int(t[i])*(3 if i%2 else 1)
    else:
        m = 3 if i%2 else 1

for x in range(10):
    if (n + m*x) % 10 == 0:
        print(x)
        break
