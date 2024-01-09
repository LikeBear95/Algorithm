def solution(my_string, queries):
    for query in queries:
        s, e = query
        if s == e:
            pass
        elif s == 0:
            my_string = my_string[e::-1] + my_string[e+1:]
        elif e == len(my_string):
            my_string = my_string[:s] + my_string[:s-1:-1]
        else:
            my_string = my_string[:s] + my_string[e:s-1:-1] + my_string[e+1:]
        # print(my_string)
    return my_string