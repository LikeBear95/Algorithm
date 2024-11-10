n, x = map(int, input().split())
lst = list(map(int, input().split()))
new_lst = [lst[i]+lst[i+1] for i in range(n-1)]

print(min(new_lst)*x)