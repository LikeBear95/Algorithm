n = int(input())
while(n != 1):
        i = 2
        while(1):
                if n % i == 0:
                        print(i)
                        n /= i
                        break
                else:
                        i += 1