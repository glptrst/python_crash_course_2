sandwich_orders = ['al_formaggio', 'pastrami', 'caprese', 'pastrami', 'serrano', 'pastrami']
finished_sandwiches = []

print('We finished pastrami')
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print(f"A {sandwich} sandwich made.")
    finished_sandwiches.append(sandwich)

print('\nSandwiches made:')
for f in finished_sandwiches:
    print(f)
