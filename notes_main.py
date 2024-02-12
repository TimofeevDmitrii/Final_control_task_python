import work_with_csv 



fields=['id', 'Название заметки', 'Описание заметки', 'Дата создания', 'Автор']
data_csv = work_with_csv.Work_with_csv(fields)

# идентификатор, заголовок, тело заметки и дату/время создания или
# последнего изменения заметки

note_1=['1', 'note1', 'smth','15.01.2022','15.01.2022']
note_2=['2', 'note2', 'smth2','16.01.2022','17.01.2022']
notes =[]

for item in note_1, note_2:
    notes.append(dict(zip(fields, item)))

data_csv.save_data_to_csv(notes)



# notes_from_csv= data_csv.read_data_from_csv()
# if len(notes_from_csv)!=0:
#     for i in notes_from_csv:
#         print(i)
# else:
#     print("Заметок еще не было добавлено")

