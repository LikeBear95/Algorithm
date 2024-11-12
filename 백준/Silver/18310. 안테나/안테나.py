n = int(input())
lst = list(map(int, input().split()))
lst = sorted(lst)
print(lst[(n-1)//2])