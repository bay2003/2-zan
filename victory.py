def get_year_input(prompt, correct_year):
    """ Функция для получения года от пользователя и проверки его корректности. """
    while True:
        input_year = input(prompt)
        if input_year.isdigit():
            input_year = int(input_year)
            return input_year == correct_year  # Возвращает True, если ответ верный
        else:
            print('Неверный формат данных. Введите год цифрами.')

def play_game():
    """ Основная функция для проведения игры. """
    correct_answers = 0
    total_questions = 5

    correct_answers += get_year_input("Введите год рождения Мерлина Менсона: ", 1969)
    correct_answers += get_year_input("Введите год рождения Адриано Челентано: ", 1938)
    correct_answers += get_year_input("Введите год рождения Тамары Гвердцители: ", 1962)
    correct_answers += get_year_input("Введите год рождения Дмитрия Маликова: ", 1970)
    correct_answers += get_year_input("Введите год рождения Николая Расторгуева: ", 1957)

    # Выводим количество правильных и неправильных ответов
    print(f"Правильных ответов: {correct_answers} из {total_questions}.")
    print(f"Неправильных ответов: {total_questions - correct_answers}.")

    # Предложение сыграть еще раз
    if input("Хотите сыграть еще раз? (да/нет): ").lower() == 'да':
        play_game()

play_game()