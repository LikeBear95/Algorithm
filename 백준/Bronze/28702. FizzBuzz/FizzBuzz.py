a = input()
b = input()
c = input()

if a.isdecimal():
    if (int(a)+3) % 3 == 0 and (int(a)+3) % 5 == 0:
        print("FizzBuzz")
    elif (int(a)+3) % 3 == 0:
        print("Fizz")
    elif (int(a)+3) % 5 == 0:
        print("Buzz")
    else:
        print(int(a)+3)
elif b.isdecimal():
    if (int(b)+2) % 3 == 0 and (int(b)+2) % 5 == 0:
        print("FizzBuzz")
    elif (int(b)+2) % 3 == 0:
        print("Fizz")
    elif (int(b)+2) % 5 == 0:
        print("Buzz")
    else:
        print(int(b)+2)
elif c.isdecimal():
    if (int(c)+1) % 3 == 0 and (int(c)+1) % 5 == 0:
        print("FizzBuzz")
    elif (int(c)+1) % 3 == 0:
        print("Fizz")
    elif (int(c)+1) % 5 == 0:
        print("Buzz")
    else:
        print(int(c)+1)