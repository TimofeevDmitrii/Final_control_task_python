from auxilary import NotesMenu
from auxilary import WorkWithCSV
from all_menu_operations import AllMenuOperations



fields=['id','Дата создания','Дата изменения', 'Название заметки', 'Описание заметки']
read_data=WorkWithCSV().read_data_from_csv()
using_operation=AllMenuOperations()
menu=NotesMenu()

all_notes_list=read_data

choice=menu.show_menu()
while (choice!=8):
    if (using_operation.contains_key(choice)):
        curr_operation=using_operation.get_operation(choice)
        curr_operation.make(all_notes_list)
    choice=menu.show_menu()
