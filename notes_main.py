import datetime
import work_with_csv
import work_with_notes
import notes_view 
import menu_notes



fields=['id','Дата создания','Дата изменения', 'Название заметки', 'Описание заметки']
data_csv = work_with_csv.WorkWithCSV(fields)
data_work=work_with_notes.WorkWithNotes()
data_view=notes_view.NotesView()
menu=menu_notes.NotesMenu()

# идентификатор, заголовок, тело заметки и дату/время создания или
# последнего изменения заметки

# note_1=['10004', 'note1','15.01.2022','Egor', 'ооооочень длинная заметка000000000000000 yyeeeeeee jjjjj lkbyyfz, ну оооочоень длинная заметка что аж капец']
# note_2=['205', 'note2','12.12.2020','Timofey', 'Какое-то описание']
# notes =[]

# for item in note_1, note_2:
#     notes.append(dict(zip(fields, item)))

# data_csv.save_data_to_csv(notes)



all_notes= data_csv.read_data_from_csv()
# print(notes_from_csv)
data_view.print_notes(all_notes)

# data_work.add_new_note(all_notes)
# data_view.print_notes(all_notes)
# data_csv.save_data_to_csv(all_notes)

# data_view.print_notes(data_work.find_note_by_id(all_notes))

# data_view.print_notes(data_work.find_notes_by_date(all_notes,'Дата создания'))



# while(choice not in [3,4]):
find_choice=menu.show_find_menu()
while(find_choice not in range(1,5)):
    find_choice=menu.show_find_menu()
if (find_choice!=4):
    note_index_for_edit=''
    if (find_choice in [1,2]):
        find_lst=data_work.find_notes_by_date(all_notes, fields[find_choice])
        if (len(find_lst)==0):
            print("Не найдено заметок с такой датой или возникла ошибка при вводе даты поиска")
        elif (len(find_lst)==1):
            note_index_for_edit=data_work.find_note_index(all_notes, find_lst[0]['id'])
        else:
            data_view.print_notes(find_lst)
            message="Найдено несколько заметок с такой "+ fields[find_choice].replace('Дата','датой')+';\nВведите дополнительно id для поиска:'
            note_index_for_edit=data_work.find_note_index(all_notes, input(message))
            # if (type(note_index_for_edit)==str):
    else:
        note_index_for_edit=data_work.find_note_index(all_notes, input("Ввeдите id заметки для поиска"))

    if(type(note_index_for_edit)==str):
        print(note_index_for_edit)
    else:
        edit=False
        edit_note=all_notes[note_index_for_edit].copy()
        data_view.print_notes([all_notes[note_index_for_edit]])
        edit_choice=menu.show_edit_menu()
        while(edit_choice not in [3,4]):
            if (edit_choice in [1,2]):
                data_work.get_correct_data(edit_note, fields[edit_choice+2])
                edit=True
            edit_choice=menu.show_edit_menu()
        if(edit_choice==4 and edit==True): 
            print("Заметка изменена")
            edit_note['Дата изменения']=datetime.date.today().strftime('%d.%m.%Y')
            all_notes[note_index_for_edit]=edit_note
            data_view.print_notes([all_notes[note_index_for_edit]])
            data_csv.save_data_to_csv(all_notes)
else:
    menu.show_menu()




