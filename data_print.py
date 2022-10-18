
def print_choice():  #выбор данных для вывода
    print("Выберите, что вы хотите вывести?\n\
        1 - данные одного ученика,\n\
        2 - список учеников одного класса,\n\
        3 - учеников по году рождения,\n\
        4 - учеников по успеваемости,\n\
        5 - всю базу данных\n\n")
    choic = input ('Ваш выбор: ')
    return choic

def choice(choic):  #определение функции печати
    if choic ==1:
        print_one_student()
    # elif print_choice ==2:
    #     print_student_class()
    # elif print_choice ==3:
    #     print_students_years()
    # elif print_choice ==4:
    #     print_students_achievement()
    # else:
    #     print_everyone_students()

def print_one_student():
    num=int(input('Введите ID ученика: '))
    with open("student_info.json") as f:
        lines = f.readlines()
        print(lines[num])
    f.close()

# def print_students_class():

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
y=print_choice()
choice(y)
print_one_student()
repeat_or_no()