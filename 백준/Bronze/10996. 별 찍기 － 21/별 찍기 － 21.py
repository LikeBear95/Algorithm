o = ' *'*50
e = '* '*50

n = int(input())
for i in range(n*2):
    print(o[:n] if i%2 else e[:n])