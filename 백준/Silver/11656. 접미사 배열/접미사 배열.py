s = input()

lst = [s[i:] for i in range(len(s))]
for i in sorted(lst):
    print(i)
