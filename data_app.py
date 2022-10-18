stud_card = {
        'ID': ['05'],
        'Имя' : ['Мария'],
        'Фамилия': ['Пастернак'],
        'Дата рождения' : ['08.03.2004'],
        'Успеваемость' : ['Хорошист']
}
with open('student_info.json', 'a') as data:
        data.write(f'{stud_card}\n')
        print(f'Результат {stud_card}\n' )
data.close()