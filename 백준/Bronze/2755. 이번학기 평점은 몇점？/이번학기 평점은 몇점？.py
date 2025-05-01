import sys
from decimal import Decimal, ROUND_HALF_UP, getcontext

input = sys.stdin.readline
getcontext().prec = 6  # 충분한 정밀도 설정

grade = {
    "A+": Decimal("4.3"), "A0": Decimal("4.0"), "A-": Decimal("3.7"),
    "B+": Decimal("3.3"), "B0": Decimal("3.0"), "B-": Decimal("2.7"),
    "C+": Decimal("2.3"), "C0": Decimal("2.0"), "C-": Decimal("1.7"),
    "D+": Decimal("1.3"), "D0": Decimal("1.0"), "D-": Decimal("0.7"),
    "F": Decimal("0.0")
}

hour = Decimal("0")
total = Decimal("0")

for _ in range(int(input())):
    _, h, g = input().split()
    h = Decimal(h)
    hour += h
    total += h * grade[g]

# 소수점 둘째 자리에서 반올림
avg = (total / hour).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
print(avg)
