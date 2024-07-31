import sys
input = sys.stdin.readline

jae = input().rstrip()
doc = input().rstrip()

print("no" if len(jae) < len(doc) else "go")
