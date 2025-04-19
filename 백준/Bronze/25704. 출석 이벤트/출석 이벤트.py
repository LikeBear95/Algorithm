n = int(input())
p = int(input())
cost = [p]

if n >= 20:
    cost.append(int(p*0.75))
if n >= 15:
    cost.append(0 if p<2000 else p-2000)
if n >= 10:
    cost.append(int(p*0.9))
if n >= 5:
    cost.append(0 if p<500 else p-500)

print(min(cost))