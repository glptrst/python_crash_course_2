import json

try:
    with open('fav_num.txt') as f:
        favorite_number = json.load(f)
        print(f'Your favorite number is {favorite_number}')
except FileNotFoundError:
    favorite_number = input('Favorite number: ')
    with open('fav_num.txt', 'w') as f:
        json.dump(favorite_number, f)

