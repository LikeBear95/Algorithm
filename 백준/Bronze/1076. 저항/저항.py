import sys
input = sys.stdin.readline

color = ["black", "brown", "red", "orange", "yellow",
         "green", "blue", "violet", "grey", "white"]

val_ten = input().rstrip()
val_one = input().rstrip()
val_unit = input().rstrip()

print((color.index(val_ten) * 10 +  color.index(val_one)) * 10 ** color.index(val_unit))
