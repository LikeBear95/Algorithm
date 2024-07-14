import sys
input = sys.stdin.readline

def star(start, num, pattern):
    if 3 ** start == num:
        return '\n'.join(pattern)
    else:
        new_pattern = []
        for p in pattern:
            new_pattern.append((p * 3))
        for p in pattern:
            new_pattern.append(p + ' '*3**start + p)
        for p in pattern:
            new_pattern.append(p * 3)
        return star(start+1, num, new_pattern)

def inputNum(n):
    return star(0, n, ["*"])


print(inputNum(int(input())))
