def solution(my_string):
    answer = ''
    delete_list = ['a', 'e', 'i', 'o', 'u']
    for string in my_string:
        if not string in delete_list:
            answer += string
    return answer