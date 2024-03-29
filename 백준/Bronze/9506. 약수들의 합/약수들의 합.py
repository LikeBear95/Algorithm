while(1):
        n = int(input())
        if n == -1:
                break
        lst = []
        for i in range(1, n):
                if n % i == 0:
                        lst.append(i)

        if n == sum(lst):
                print(f'{n} = {" + ".join(map(str, lst))} ')
        else:
                print(f'{n} is NOT perfect.')