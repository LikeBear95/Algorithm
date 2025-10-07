import sys
input = sys.stdin.readline

dna = {"AA":"A", "GA":"C", "CA":"A", "TA":"G", 
       "AG":"C", "GG":"G", "CG":"T", "TG":"A", 
       "AC":"A", "GC":"T", "CC":"C", "TC":"G", 
       "AT":"G", "GT":"A", "CT":"G", "TT":"T",}

n = int(input())
s = list(input().rstrip())

for i in range(n-1, 0, -1):
    s[i-1] = dna[s[i-1] + s[i]]

print(s[0])