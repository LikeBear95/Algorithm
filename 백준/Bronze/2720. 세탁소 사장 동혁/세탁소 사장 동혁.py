cent = [25, 10, 5, 1]
for tc in range(int(input())):
        lst = []
        money = int(input())
        for i in cent:
                lst.append(money // i)
                money %= i
        print(*lst)