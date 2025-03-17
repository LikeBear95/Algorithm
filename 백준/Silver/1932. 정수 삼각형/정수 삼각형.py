import sys
input = sys.stdin.readline

n = int(input())
nums = [list(map(int, input().split()))]
sums = [nums[0]]

for i in range(1, n):
    nums.append(list(map(int, input().split())))
    tmp = []
    for j in range(i+1):
        if j == 0 or j == i:
            tmp.append(nums[i][j]+(sums[i-1][i-1] if j else sums[i-1][0]))
        else:
            tmp.append(nums[i][j]+max(sums[i-1][j], sums[i-1][j-1]))
    sums.append(tmp)
        
print(max(sums[-1]))