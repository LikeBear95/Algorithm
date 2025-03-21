s = input()
x = 0
for i in s:
    if i in ['A','a','b','D','d','e','g','O','o','P','p','Q','q','R','@']:
        x += 1
    elif i == 'B':
        x += 2
print(x)