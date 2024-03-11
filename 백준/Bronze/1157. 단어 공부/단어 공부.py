word = input().upper()
alpha = list(set(word))
maxcount = 0
maxalpha = '?'

for i in alpha:
    if word.count(i) > maxcount:
        maxcount = word.count(i)
        maxalpha = i
    elif word.count(i) == maxcount and i != maxalpha:
        maxalpha = '?'

print(maxalpha)