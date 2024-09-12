lst = [0]
for i in range(int(input())):
    lst.append(int(input()))
    
answer = 0
for j in range(int(input())):
    answer += lst[int(input())]
    
print(answer)