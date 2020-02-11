def count_word(file_name, word):
    try:
        with open(file_name, encoding='utf-8') as f:
            content = f.read()
            number = content.lower().count(word)
            print(f"'{file_name}' has {number} '{word}'")
    except:
        print('Some error occurred')

books = ['darkness.txt', 'earnest.txt', 'moby_dick.txt']

for book in books:
    count_word(book, 'the')
    
for book in books:
    count_word(book, 'the ')
