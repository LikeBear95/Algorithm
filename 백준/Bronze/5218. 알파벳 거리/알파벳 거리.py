import sys
input = sys.stdin.readline

alpha = {"A":1, "B":2, "C":3, "D":4,"E":5,
         "F":6, "G":7, "H":8, "I":9, "J":10,
         "K":11, "L":12, "M":13, "N":14,"O":15,
         "P":16, "Q":17, "R":18, "S":19, "T":20,
         "U":21, "V":22, "W":23, "X":24,"Y":25, "Z":26}

for _ in range(int(input())):
    a, b = map(str, input().rstrip().split())
    d = [alpha[b[i]] - alpha[a[i]] + 26 if alpha[b[i]] - alpha[a[i]] < 0 else alpha[b[i]] - alpha[a[i]] for i in range(len(a))]
    print(f'Distances: {" ".join(str(x) for x in d)}')
