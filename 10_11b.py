import json

with open('fav_num.txt') as f:
    favorite_number = json.load(f)

print(f'Your favorite number is {favorite_number}')
