num = {'zero': '0', 'one': '1', 'two': '2', 'three': '3', 'four': '4',
      'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}
def solution(numbers):
    answer = 0
    tmp = 0
    word = ''
    for index in range(len(numbers)):
        if numbers[tmp:index + 1] in num:
            word += num[numbers[tmp:index + 1]]
            tmp = index + 1
    answer = int(word)
    return answer