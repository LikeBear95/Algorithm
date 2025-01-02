n, x = map(int, input().split())
lst = list(map(int, input().split()))
new_lst = [sum(lst[:x])]

for i in range(n-x):
    new_lst.append(new_lst[i] - lst[i] + lst[i+x])

m = max(new_lst)
if m == 0:
    print("SAD")
else:
    print(m)
    print(new_lst.count(m))