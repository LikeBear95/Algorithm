import sys
input = sys.stdin.readline

while True:
    l = input().rstrip()
    if l == "#":
        break
    print(l.count("a")+l.count("e")+l.count("i")+l.count("o")+l.count("u")+l.count("A")+l.count("E")+l.count("I")+l.count("O")+l.count("U"))