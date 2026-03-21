import sys
input = sys.stdin.readline

days = {
    1:31, 2:29, 3:31, 4:30, 5:31, 6:30,
    7:31, 8:31, 9:30, 10:31, 11:30, 12:31
}

def HM(h, m):
    return 0 <= h <= 23 and 0 <= m <= 59

def MD(m, d):
    return m in days and 1 <= d <= days[m]

for _ in range(int(input())):
    x, y = map(int, input().split())
    
    print("Yes" if HM(x, y) else "No", end=" ")
    print("Yes" if MD(x, y) else "No")