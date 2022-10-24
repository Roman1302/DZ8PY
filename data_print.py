from pprint import pprint
import json
import data_print as dp


def print_choice():  #выбор данных для вывода
    print("Выберите, что вы хотите вывести?\n\
        1 - данные ученика,\n\
        2 - список учеников одного класса,\n\
        3 - учеников по году рождения,\n\
        4 - учеников по успеваемости,\n\
        5 - всю базу данных\n\n")
    choic = input ('Ваш выбор: ')
    return choic

def print_one_student(): # печать одного ученика
    fam=input('Введите фамилию ученика: ')
    with open("student_info.json", "r", encoding="utf-8") as f:
        text = json.load(f)
    for tex in text["stud_card"]:
        if fam == tex["family"]:
            print(f'{tex["name"]} {tex["family"]}, {tex["birthdate"]},\
класс:{tex["classroom"]}, {tex["achievement"]}')
    f.close()

def print_students_class(): # печать списка из класса
    clas=input('Введите класс (с 1 по 11): ')
    with open("student_info.json", "r", encoding="utf-8") as f:
        text = json.load(f)
    for tex in text["stud_card"]:
        if clas == tex["classroom"]:
            print(f'{tex["name"]} {tex["family"]}, {tex["birthdate"]}, \
класс:{tex["classroom"]}, {tex["achievement"]}')
    f.close()

def print_students_years(): # печать списка по году рождания
    year=int(input('Введите год рождения: '))
    with open("student_info.json", "r", encoding="utf-8") as f:
        text = json.load(f)
    for tex in text["stud_card"]:
        yyyy = int(str(tex["birthdate"])[6:10])
        if year <= yyyy<= year:
            print(f'{tex["name"]} {tex["family"]}, {tex["birthdate"]}, \
класс:{tex["classroom"]}, {tex["achievement"]}')
    f.close()

def print_students_achievement(): # печать по успеваемости
    achiev=input('Введите успеваемость(отличник, хорошист, троичник, неуспевающий): ')
    with open("student_info.json", "r", encoding="utf-8") as f:
        text = json.load(f)
    for tex in text["stud_card"]:
        if achiev == tex["achievement"]:
            print(f'{tex["name"]} {tex["family"]}, {tex["birthdate"]},\
класс:{tex["classroom"]}, {tex["achievement"]}')
    f.close()
    
def print_everyone_students(): # печать всего списка
    print('Общий список: ')
    with open("student_info.json", "r", encoding="utf-8") as f:
        text = json.load(f)
    for tex in text["stud_card"]:
        print(f'{tex["name"]:<10}{tex["family"]:<15}\
        {tex["birthdate"]:>5}  класс: {tex["classroom"]:<3}{tex["achievement"]:>12}\n', "-"*70)
    f.close()

def choice(choic):  #определение функции печати
    if choic =="1":
        print_one_student()
    elif choic =="2":
        print_students_class()
    elif choic =="3":
        print_students_years()
    elif choic =="4":
        print_students_achievement()
    else:
        print_everyone_students()

def repeat_or_no():
    # Функция для запроса пользователя продолжить или нет
    user_choice = 'Плохой ответ'
    while user_choice != 'Y' or user_choice != 'N':
        user_choice = input('Вы хотите продолжить работу с базой учеников? (Y или N): ')
        if user_choice == 'N':
            return False
        elif user_choice == 'Y':
            dp.choice(dp.print_choice())
        else:
            print('Неверный ответ! Вы хотите продолжить работу с базой? Вставить Y или N: ')