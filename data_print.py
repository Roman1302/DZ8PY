from pprint import pprint
import jmespath
import json
import datetime


def print_choice():  #выбор данных для вывода
    print("Выберите, что вы хотите вывести?\n\
        1 - данные ID ученика,\n\
        2 - список учеников одного класса,\n\
        3 - учеников по году рождения,\n\
        4 - учеников по успеваемости,\n\
        5 - всю базу данных\n\n")
    choic = input ('Ваш выбор: ')
    return choic

"""def print_one_student(): # печать одного ученика
    fam=input('Введите фамилию ученика: ')
    # print(fam)
    with open("student_info.json", "r", encoding="utf-8") as f:
        text = json.load(f)
        # pprint(text)
    for tex in text["stud_card"]:
        # print(tex["family"])
        if fam == tex["family"]:
            print(f'{tex["name"]} {tex["family"]}, {tex["birthdate"]},\
             класс:{tex["classroom"]}, {tex["achievement"]}')
        # print(text["stud_card"][0]["Имя"])

    f.close()

def print_students_class(): # печать списка из класса
    clas=input('Введите класс: ')
    with open("student_info.json", "r", encoding="utf-8") as f:
        text = json.load(f)
        # pprint(text)
    for tex in text["stud_card"]:
        # print(tex["family"])
        if clas == tex["classroom"]:
            print(f'{tex["name"]} {tex["family"]}, {tex["birthdate"]}, \
класс:{tex["classroom"]}, {tex["achievement"]}')
    f.close()"""

def print_students_years(): # печать списка по году рождания
    year=int(input('Введите год рождения: '))
    with open("student_info.json", "r", encoding="utf-8") as f:
        text = json.load(f)
    for tex in text["stud_card"]:
        yyyy = int(str(tex["birthdate"])[6:10])
        # print(yyyy)
        if year <= yyyy<= year:
            print(f'{tex["name"]} {tex["family"]}, {tex["birthdate"]}, \
класс:{tex["classroom"]}, {tex["achievement"]}')
    f.close()


def choice(choic):  #определение функции печати
    if choic =="1":
        print_one_student()
    elif choic =="2":
        print_students_class()
    elif choic =="3":
        print_students_years()
    # elif choic ==4:
    #     print_students_achievement()
    # else:
    #     print_everyone_students()





# def print_students_years():

# def print_students_achievement():

# def print_everyone_students():



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

choice(print_choice())
