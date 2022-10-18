import datetime

def data_entry():
    # Функция приглашает пользователя внести данных учеников и сохранить их в файл
    print('Журнал заполнения\n')
    name = input('Введите имя ученика: ')
    family = input('Введите фамилию ученика: ')
    while True: #запускает проверку правильной даты
        try:
            birthdate = input('Введите дату рождения ученика в форме ДД.ММ.ГГГГ: ')
            if datetime.datetime.strptime(birthdate, '%d.%m.%Y'):
                break
            else:
                print("Неправильный формат данных, должен быть ДД.ММ.ГГГГ")
        except:
            print("Ошибка - это не дата")
    classroom = input('Введите класс ученика: ')
    achievement = input('Введите успеваемость ученика: ')

    print(f'Вы ввели данные: {name} {family} {birthdate} {classroom} {achievement}\n')

    stud_card = {
        'ID': [len(open('student_info.json').readlines())],
        'Имя' : [name],
        'Фамилия': [family],
        'Дата рождения' : [birthdate],
        'Класс' :[classroom],
        'Успеваемость' : [achievement]
        }
    with open('student_info.json', 'a') as data:
        data.write(f'{stud_card}\n')

    data.close()

def repeat_or_no():
    # Функция для запроса пользователя продолжить или нет
    user_choice = 'Выбор'
    while user_choice != 'Y' or user_choice != 'N':
        user_choice = input('Вы хотите продолжить ввод данных? (Y или N): ')
        if user_choice == 'N':
            return False
        elif user_choice == 'Y':
            return True
        else:
            print('Неверный ответ! Вы хотите продолжить работу? Вставить Y или N: ')

