def delete_stud_card(stud_card, identifier, name, surname,date_of_birth,academic_performance):
    for i in range(len(stud_card)):
        if(" ".join(stud_card[i][0]) == identifier and stud_card[i][1] == name and stud_card[i][2] == surname and stud_card[i][3] == date_of_birth and stud_card[i][4]== academic_performance and stud_card[i][5]):
            stud_card.pop(i);
            return stud_card
    print("Такого студента не существует!")