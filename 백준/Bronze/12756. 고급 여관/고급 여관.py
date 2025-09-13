aa, ab = map(int, input().split())
ba, bb = map(int, input().split())

while ab > 0 and bb > 0:
    ab -= ba
    bb -= aa

if ab <= 0 and bb <= 0:
    print("DRAW")
elif bb <= 0:
    print("PLAYER A")
else:
    print("PLAYER B")
