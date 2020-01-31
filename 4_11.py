pizzas = ['marinara', 'margherita', 'capricciosa']

friend_pizzas = pizzas[:]

pizzas.append("quattro stagioni")
friend_pizzas.append("boscaiola")

print("My favorite pizzas are:")
for pizza in pizzas:
    print(pizza)

print("\nMy friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print(pizza)
