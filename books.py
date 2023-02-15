class books:
    def __init__(self, name, author, date, genre, country):
        self.name = name
        self.author = author
        self.date = date
        self.genre = genre
        self.country = country


    def get_data(self):
        data = {
            'Название': self.name,
            'Автор': self.author,
            'Год выпуска': self.date,
            'Жанр': self.genre,
            'Страна выпуска': self.country
        }
        return data

name = input('Введите название книги: ')
author = input('Введите автора книги: ')
def looking_for_error_in_date():
    try:
        date_def = int(input('Введите год выпуска книги: '))
        return date_def
    except:
        print('Ввы ввели не числовое значение')
        looking_for_error_in_date()
date = looking_for_error_in_date()
genre = input('Введите жанр книги: ')
country = input('Введите страну выпуска: ')
book_info = books(name, author, date, genre, country)
print(book_info.get_data())
