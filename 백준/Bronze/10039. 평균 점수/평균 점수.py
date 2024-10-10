answer = 0
for _ in range(5):
    n = int(input())
    answer += n if n >= 40 else 40
    
print(answer//5)