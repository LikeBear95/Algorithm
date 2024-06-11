import sys
from collections import deque

deck = deque()
for _ in range(int(sys.stdin.readline())):
    tmp = sys.stdin.readline().rstrip()
    if tmp[0] == "1":
        deck.appendleft(int(tmp[2:]))
    elif tmp[0] == "2":
        deck.append(int(tmp[2:]))
    elif tmp[0] == "3":
        print(deck.popleft() if deck else -1)
    elif tmp[0] == "4":
        print(deck.pop() if deck else -1)
    elif tmp[0] == "5":
        print(len(deck))
    elif tmp[0] == "6":
        print(0 if deck else 1)
    elif tmp[0] == "7":
        print(deck[0] if deck else -1)
    elif tmp[0] == "8":
        print(deck[-1] if deck else -1)
