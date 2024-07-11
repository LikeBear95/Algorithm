import sys
from collections import Counter
input = sys.stdin.readline

n = int(input())
lst = [int(input()) for _ in range(n)]

counter = Counter(lst)
most_common = counter.most_common()
max_freq = most_common[0][1]
cnts = [num for num, freq in most_common if freq == max_freq]

print(round(sum(lst)/n))
print(sorted(lst)[n//2])
print(sorted(cnts)[1] if len(cnts) > 1 else cnts[0])
print(max(lst) - min(lst))
