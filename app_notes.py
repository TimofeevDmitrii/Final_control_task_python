from auxilary import NotesMenu
from auxilary import WorkWithCSV
from all_menu_operations import AllMenuOperations
import traceback


fields=['id','Дата создания','Дата изменения', 'Название заметки', 'Описание заметки']
read_data=WorkWithCSV(fields).read_data_from_csv()
using_operation=AllMenuOperations()
menu=NotesMenu()

try:
    all_notes_list=read_data

    choice=menu.show_menu()
    while (choice!=8):
        if (using_operation.contains_key(choice)):
            curr_operation=using_operation.get_operation(choice)
            curr_operation.make(all_notes_list)
        print()
        choice=menu.show_menu()
except Exception as e:
    print("\n--->В ходе работы программы произошла ошибка. Возможно файл Notes.csv был поврежден")
    print("--->Завершение работы.")
    print(e, traceback.format_exc())
