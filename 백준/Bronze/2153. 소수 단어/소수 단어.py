s = input()
n = 0

for t in s:
    n += ord(t)-38 if t.isupper() else ord(t)-96

for i in range(2, int(n**0.5)+1):
    if not n%i:
        print("It is not a prime word.")
        break
else:
    print("It is a prime word.")