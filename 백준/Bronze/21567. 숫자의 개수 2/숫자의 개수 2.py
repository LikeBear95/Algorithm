d = {"0":0, "1":0, "2":0, "3":0, "4":0, "5":0, "6":0, "7":0, "8":0, "9":0}
a = int(input())
b = int(input())
c = int(input())

for i in str(a*b*c):
    d[i] += 1

for i in range(10):
    print(d[str(i)])