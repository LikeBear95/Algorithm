cube = [i**3 for i in range(101)]

for a in range(2,101):
    for b in range(2,a):
        for c in range(b,a):
            for d in range(c,a):
                if cube[b]+cube[c]+cube[d]==cube[a]:
                    print(f"Cube = {a}, Triple = ({b},{c},{d})")