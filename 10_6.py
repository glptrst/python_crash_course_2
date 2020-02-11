try:
    first_number = int(input('1st number: '))
    second_number = int(input('2nd number: '))
except:
    print('You gotta give me a number')
else:
    print(f'Result is {first_number + second_number}')


