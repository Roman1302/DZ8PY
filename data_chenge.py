def get_stud_card(s, student_list):
    s = s.replace(';', "")
    list_of_student_temp = s.split(" ") #список, в котором храним новых студентов
    
    while(len(list_of_student_temp) != 0):
        about_student = []
        about_student.append(int(list_of_student_temp[1]))# identifier номер
        about_student.append(list_of_student_temp[2])# name имя
        about_student.append(list_of_student_temp[3])# surname фамилия
        about_student.append(int(list_of_student_temp[4]))# date_of_birth дата рождения 
        about_student.append(list_of_student_temp[5])# academic_performance успеваемость
        student_list.append(about_student)
        list_of_student_temp = list_of_student_temp[8:]
    return student_list
    