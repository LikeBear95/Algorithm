nums =[]
for i in range(28):
    nums.append(int(input()))

for j in range(1, 31):
    if not j in nums:
        print(j)