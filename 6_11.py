cities = {
    'barcelona': {
        'country': 'spain',
        'population': 5,
    },
    'berlin': {
        'country': 'germany',
        'population': 15
    }
}

for city, info in cities.items():
    print(f'{city.title()}:')
    for k, v in info.items():
        print(f'{k.title()}: {v}')
    print('---')
