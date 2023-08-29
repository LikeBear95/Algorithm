def find_answer(lst, tri):
    for v, num in enumerate(lst):
        cnt = 0
        if len(num) != len(tri):
            continue
        else:
            for i in range(len(num)):
                if num[i] != tri[i]:
                    cnt += 1
                if cnt > 1:
                    break
            else:
                if cnt == 1:
                    return v

T = int(input())
for t in range(1, T + 1):
    bin = list(input())
    tri = input()
    bin_lst = []

    for i in range(1, len(bin)):
        temp = ''
        for j in range(len(bin)):
            if i == j and bin[i] == '0':
                temp += '1'
            elif i == j and bin[i] == '1':
                temp += '0'
            else:
                temp += bin[j]
        bin_lst.append(temp)

    deci_lst = []
    for num in bin_lst:
        temp = 0
        for i in range(len(num)):
            temp += int(num[i]) * 2 ** (len(num) - i - 1)
        deci_lst.append(temp)

    tri_lst = []
    for num in deci_lst:
        temp = ''
        while num:
            temp += str(num % 3)
            num //= 3
        tri_lst.append(temp[::-1])

    result = deci_lst[find_answer(tri_lst, tri)]


    print(f'#{t} {result}')
