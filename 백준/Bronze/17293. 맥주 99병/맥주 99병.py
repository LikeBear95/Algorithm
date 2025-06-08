n = int(input())

for i in range(n,-1,-1):
    if i == 0:
        print(f"No more bottles of beer on the wall, no more bottles of beer.")
        print(f"Go to the store and buy some more, {n} bottle{'' if n == 1 else 's'} of beer on the wall.")
    else:
        print(f"{i} bottle{'' if i == 1 else 's'} of beer on the wall, {i} bottle{'' if i == 1 else 's'} of beer.")
        print(f"Take one down and pass it around, {'no more' if i == 1 else i-1} bottle{'' if i == 2 else 's'} of beer on the wall.")
        print("")
