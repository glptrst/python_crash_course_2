while True:
    try:
        first_number = input('1st number: ')
        if first_number == 'q':
            break
        second_number = input('2nd number: ')
        if second_number == 'q':
            break
        first_number = int(first_number)
        second_number = int(second_number)
    except:
        print('You gotta give me a number')
        continue
    else:
        print(f'Result is {first_number + second_number}')


