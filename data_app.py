

def data_entry():
    # Функция приглашает пользователя внести данных учеников и сохранить их в файл
    print('Журнал заполнения\n')
    name = input('Введите имя ученика: ')
    family = input('Введите фамилию ученика: ')
    birthdate = input('Введите дату рождения ученика: ')
    achievement = input('Введите успеваемость ученика: ')
    print(f'Вы ввели данные: {name} {family} {birthdate} {achievement}\n')
# print(len(open('student_info.json').readlines()))

    stud_card = {
        'ID': [len(open('student_info.json').readlines())],
        'Имя' : [name],
        'Фамилия': [family],
        'Дата рождения' : [birthdate],
        'Успеваемость' : [achievement]
        }
    with open('student_info.json', 'a') as data:
        data.write(f'{stud_card}\n')
#     print(f'Вы ввели данные: {stud_card}\n' )
    data.close()
data_entry()