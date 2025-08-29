import sys
input = sys.stdin.readline

for _ in range(int(input())):
    t = input().rstrip()
    
    cm, y, ssu, ssa, f = map(int, input().rstrip().split())
    cm, y, ssu, ssa, f = cm//(8/16), y//(8/16), ssu//(4/16), ssa*16, f//(9/16)
    cake = int(min(cm, y, ssu, ssa, f))
    
    b, gs, gc, w = map(int, input().rstrip().split())
    b, gs, gc, w = b, gs//30, gc//25, w//10
    topping = sum([b, gs, gc, w])
    
    print(min(cake, topping))