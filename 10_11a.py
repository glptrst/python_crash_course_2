import json

favorite_number = input('Favorite number: ')

with open('fav_num.txt', 'w') as f:
    json.dump(favorite_number, f)
    
