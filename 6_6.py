favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'ruby',
'phil': 'python',
}

people = ['john', 'jen', 'filippo', 'phil']

for p in people:
    if p in set(favorite_languages.keys()):
        print(f'Thank you, {p}, for having taken the poll.')
    else:
        print(f'Hey {p}, please take the poll!')


