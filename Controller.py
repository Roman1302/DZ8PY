from timeit import repeat
import data_chenge
import data_app as da
import data_delete
import data_print as dp

def sort_data(number):
    while True: 
        d = number
        if d=="1":
            da.data_entry()
            da.repeat_or_no()
            break
        elif d=="2":
            data_chenge.get_stud_card()
        elif d=="3":
            data_delete.get_stud_card() 
        elif d=="4":
            dp.choice(dp.print_choice())
            dp.repeat_or_no()
            break      
        else:
            print('До свидания!')        
            break