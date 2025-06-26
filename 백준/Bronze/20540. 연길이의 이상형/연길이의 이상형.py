s = input()
a = ''
for i in s:
    if i in ['E', 'I']:
        a += 'E' if i == 'I' else 'I'
    elif i in ['S', 'N']:
        a += 'S' if i == 'N' else 'N'
    elif i in ['T', 'F']:
        a += 'T' if i == 'F' else 'F'
    else:
        a += 'J' if i == 'P' else 'P'
print(a)