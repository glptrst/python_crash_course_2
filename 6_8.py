billy = {
    'kind': 'dog',
    'owner': 'john'
}

fuf = {
    'kind': 'cat',
    'owner': 'matt'
}

pets = [billy, fuf]

for p in pets:
    for k, v in p.items():
        print(f'{k}: {v}')
    print('---')
