import sys
input = sys.stdin.readline

grade = {
    "A+": 4.3, "A0": 4.0, "A-": 3.7,
    "B+": 3.3, "B0": 3.0, "B-": 2.7,
    "C+": 2.3, "C0": 2.0, "C-": 1.7,
    "D+": 1.3, "D0": 1.0, "D-": 0.7,
    "F": 0.0
}

hour = 0
total = 0
for _ in range(int(input())):
    _, h, g = input().split()
    h = int(h)
    hour += h
    total += h * grade[g]

# 수동 반올림 (소수점 셋째 자리에서 반올림)
avg = total / hour
avg = int(avg * 100 + 0.5) / 100
print(f"{avg:.2f}")