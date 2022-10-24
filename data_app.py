import datetime
import json
import data_app as da


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
        "name" : name,
        "family": family,
        "birthdate" : birthdate,
        "classroom": classroom,
        "achievement" : achievement}
    with open("student_info.json", encoding='utf-8') as f:
        data=json.load(f)
        data["stud_card"].append(stud_card)
        with open("student_info.json", "w", encoding="utf-8") as fh:
            json.dump(data, fh, ensure_ascii=False, indent=2)
            fh.close()
        f.close()
    
def repeat_or_no():
    # Функция для запроса пользователя продолжить или нет
    user_choice = 'Плохой ответ'
    while user_choice != 'Y' or user_choice != 'N':
        user_choice = input('Вы хотите продолжить работу с базой учеников? (Y или N): ')
        if user_choice == 'N':
            return False
        elif user_choice == 'Y':
            da.data_entry()
        else:
            print('Неверный ответ! Вы хотите продолжить работу с базой? Вставить Y или N: ')
