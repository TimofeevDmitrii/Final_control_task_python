import work_with_csv
import work_with_notes 



fields=['id', 'Название заметки', 'Дата создания', 'Автор', 'Описание заметки']
data_csv = work_with_csv.WorkWithCSV(fields)
data_work=work_with_notes.WorkWithNotes(fields)

# идентификатор, заголовок, тело заметки и дату/время создания или
# последнего изменения заметки

# note_1=['10004', 'note1','15.01.2022','Egor', 'ооооочень длинная заметка000000000000000 yyeeeeeee jjjjj lkbyyfz']
# note_2=['205', 'note2','12.12.2020','Timofey', 'Какое-то описание']
# notes =[]

# for item in note_1, note_2:
#     notes.append(dict(zip(fields, item)))

# data_csv.save_data_to_csv(notes)



notes_from_csv= data_csv.read_data_from_csv()
# print(notes_from_csv)
data_work.print_notes(notes_from_csv)
# if len(notes_from_csv)!=0:
#     for i in notes_from_csv:
#         print(i)
# else:
#     print("Заметок еще не было добавлено")

