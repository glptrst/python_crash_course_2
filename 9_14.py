from random import choice

foo = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'a', 'b', 'c', 'd', 'e']

for i in range(4):
    print(f"{choice(foo)} won!")


