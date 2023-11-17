answer = input('Привет, как тебя зовут? ')

# Цикл продолжается, пока 'answer' не будет содержать только буквы
while not answer.isalpha():
    print('Неверно введены данные. Пожалуйста, используйте только буквы.')
    answer = input('Как тебя зовут? ')

print('Приятно познакомиться,', answer)

print(type(answer))

while True:
    age_input = input("Сколько вам лет? ")

    # Проверяем, является ли ввод целым числом
    if age_input.isdigit():
        age = int(age_input)  # Преобразуем строку в целое число
        print(f"Вам {age} лет.")
        break
    else:
        print("Пожалуйста, введите целое число.")
print(type(age_input))

while True:
    age_input = input("Введите ваш возраст в формате 'лет,месяцев' (например, 15,5): ")

    # Проверяем, что ввод содержит только одну запятую и цифры
    if ',' in age_input and age_input.count(',') == 1:
        years, months = age_input.split(',')

        # Проверяем, что и годы, и месяцы являются цифрами
        if years.isdigit() and months.isdigit():
            years = int(years)
            months = int(months)

            # Преобразуем месяцы в долю года
            fractional_years = years + months / 12
            print(f"Ваш возраст: {fractional_years} лет.")
            break
        else:
            print("Используйте только цифры для лет и месяцев.")
    else:
        print("Пожалуйста, введите возраст в правильном формате.")

print(type(fractional_years))

def get_int_input(prompt):
    """ Функция для безопасного получения целочисленного ввода от пользователя. """
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Неверный формат данных. Пожалуйста, введите целое число.")

# Запрашиваем количество предметов
total_subjects = get_int_input("Сколько у вас предметов? ")

# Запрашиваем количество оценок по каждой категории
fives = get_int_input("Сколько у вас пятёрок? ")
fours = get_int_input("Сколько у вас четвёрок? ")
threes = get_int_input("Сколько у вас троек? ")

# Проверяем, что сумма оценок не превышает общее количество предметов
if fives + fours + threes > total_subjects:
    print("Ошибка: сумма оценок превышает количество предметов.")
else:
    # Рассчитываем общий балл
    total_points = fives * 5 + fours * 4 + threes * 3
    average = total_points / total_subjects

    # Выводим средний балл и соответствующее сообщение
    print(f"Ваш средний балл: {average:.2f}")
    if average >= 4.8:
        print("Ты почти отличник!")
    elif average >= 4:
        print("Да ты хорошист!")

print(type(total_points))
