import sys
input = sys.stdin.readline

d = {"animal":"Panthera tigris", "flower":"Forsythia koreana", "tree":"Pinus densiflora"}

while True:
    t = input().rstrip()
    if t == "end":
        break
    else:
        print(d[t])