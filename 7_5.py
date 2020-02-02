active = True

while active:
    age = input('Age? ')

    if age == 'quit':
        break;

    if int(age) < 3:
        print('free')
    elif int(age) >= 3 and int(age) <= 12:
        print('$10')
    else:
        print('$15')
