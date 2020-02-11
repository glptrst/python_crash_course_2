while True:
    name = input('Your name? ')
    if name == 'quit':
        break
    else:
        print(f'Hello {name}')
        with open('./guest_book.txt', 'a') as file_object:
            file_object.write(f'{name} visited\n')
    
