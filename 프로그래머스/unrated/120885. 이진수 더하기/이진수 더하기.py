def solution(bin1, bin2):
    answer = ''
    tmp1 = 0
    tmp2 = 0
    for i in range(len(bin1)):
        tmp1 += int(bin1[i]) * 2 ** (len(bin1) - i - 1)
    for i in range(len(bin2)):
        tmp2 += int(bin2[i]) * 2 ** (len(bin2) - i - 1)
    tmp = tmp1 + tmp2
    while(tmp):
        answer += str(tmp % 2)
        tmp //= 2
    if not answer:
        answer = "0"
    return answer[::-1]