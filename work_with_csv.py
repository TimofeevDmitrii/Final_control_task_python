import csv
import os

file_name = 'notes.csv'
fields=['id', 'head', 'body', 'date_of_creation', 'last_edit_date']

def save_data_to_csv(notes_lst):
    with open(file_name,'w',encoding='utf-8', newline='') as data_csv:
        writer = csv.DictWriter(data_csv, fields, delimiter=';')
        writer.writeheader()
        writer.writerows(notes_lst)



#идентификатор, заголовок, тело заметки и дату/время создания или
#последнего изменения заметки

def read_data_from_csv():
    notes_lst = []
    if os.path.isfile(file_name):
        with open(file_name,'r',encoding='utf-8', newline='') as data_csv:     # newline='' ???
            reader = csv.DictReader(data_csv, delimiter=';') 
            notes_lst=[i for i in reader]
    return notes_lst