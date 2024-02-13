import work_with_csv
import work_with_notes
import notes_view 



fields=['id','Дата создания','Дата изменения', 'Название заметки', 'Описание заметки']
data_csv = work_with_csv.WorkWithCSV(fields)
data_work=work_with_notes.WorkWithNotes()
data_view=notes_view.NotesView()

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

data_view.print_notes(data_work.find_note_by_id(all_notes))

# data_view.print_notes(data_work.find_notes_by_date(all_notes,'Дата создания'))

