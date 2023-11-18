while True:
    age_pushkin = input("Введите год рождения А.С. Пушкина: ")
    if age_pushkin.isdigit():
        age_pushkin = int(age_pushkin)
        if age_pushkin == 1799:
            print('Все верно')
            break
        else:
            print('Неверно')
while True:
    age_you = input("Какой день рожения у Пушкина А.С. формата 07 ")
    if age_you.isdigit():
        age_you = int(age_you)
        if age_you == 6:
            print('Спасибо за ответ')
            break
else:
    print("Неверно")
