def all_calc():
    class calc:
        def __init__(self, first_number, sigh, second_number):
            self.first_number = first_number
            self.sigh = sigh
            self.second_number = second_number

        def calculator(self):
            if self.sigh == '+':
                addition = (f'Сумма чисел равна: {self.first_number + self.second_number}')
                return addition

            elif self.sigh == '-':
                subtraction = (f'Разность чисел равна: {self.first_number - self.second_number}')
                return subtraction

            elif self.sigh == '*':
                multiplication = (f'Произведение чисел равно: {self.first_number * self.second_number}')
                return multiplication

            elif self.sigh == '/':
                if self.second_number == 0:
                    error = 'Делить на 0 нельзя'
                    return error
                else:
                    division = (f'Частное чисел равно: {self.first_number / self.second_number}')
                    return division

            else:
                sigh_error = ('Вы ввели неверный знак')
                return sigh_error

    try:
        a = int(input('Введите первое число: '))
        b = input('Введите знак: ')
        c = int(input('Введите второе число: '))
        task = calc(a, b, c)
        print(task.calculator())
    except:
        print('Нужно ввести число!')
        all_calc()

all_calc()