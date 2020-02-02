sandwich_orders = ['al_formaggio', 'caprese', 'serrano']
finished_sandwiches = []

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print(f"A {sandwich} sandwich made.")
    finished_sandwiches.append(sandwich)

print('\nSandwiches made:')
for f in finished_sandwiches:
    print(f)
