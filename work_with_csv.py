import csv
import os

class Work_with_csv:

    def __init__(self, fields, file_name):
        self.file_name=file_name
        self.fields=fields

    def save_data_to_csv(self,notes_lst):
        with open(self.file_name,'w',encoding='utf-8', newline='') as data_file_csv:
            writer = csv.DictWriter(data_file_csv, self.fields, delimiter=';')
            writer.writeheader()
            writer.writerows(notes_lst)


    def read_data_from_csv(self):
        notes_lst = []
        if os.path.isfile(self.file_name):
            with open(self.file_name,'r',encoding='utf-8', newline='') as data_file_csv: 
                reader = csv.DictReader(data_file_csv, delimiter=';') 
                notes_lst=[i for i in reader]
        return notes_lst