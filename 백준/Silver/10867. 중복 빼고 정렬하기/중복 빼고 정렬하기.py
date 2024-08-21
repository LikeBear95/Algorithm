n = int(input())
lst = list(map(int, input().split()))
print(*sorted(list(set(lst))))