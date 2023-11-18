while True:
    age_pushkin = input("Введите год рождения А.С. Пушкина: ")

    if age_pushkin.isdigit():
        age_pushkin = int(age_pushkin)
        if age_pushkin == 1799:
            print('Все верно')
            break
        else:
            print('Неверно')
    else:
        print('Неверный формат данных. Введите год цифрами.')
