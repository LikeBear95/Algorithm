import sys
input = sys.stdin.readline

for _ in range(int(input())):
    d = {"TTT":0, "TTH":0, "THT":0, "THH":0, "HTT":0, "HTH":0, "HHT":0, "HHH":0}
    t = input().rstrip()
    for i in range(len(t)-2):
        d[t[i:i+3]] += 1

    print(*d.values())
    