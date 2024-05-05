import sys
input = sys.stdin.readline

lst = set()
for _ in range(int(input())):
    name, state = input().split()
    if state == 'enter':
        lst.add(name)
    elif state == 'leave':
        lst.remove(name)

for i in sorted(lst, reverse=True):
    print(i)