matt = {
    'firt_name': 'Matt',
    'last_name': 'Berettola',
    'age': 18,
    'city': 'Barcelona'
}

dean = {
    'firt_name': 'Dean',
    'last_name': 'Berettola',
    'age': 28,
    'city': 'Lisbon'
}

maria = {
    'firt_name': 'Maria',
    'last_name': 'Fringelli',
    'age': 31,
    'city': 'Milan'
}

people = [matt, dean, maria]

for p in people:
    for k, v in p.items():
        print(f'{k}: {v}')
    print('---')
