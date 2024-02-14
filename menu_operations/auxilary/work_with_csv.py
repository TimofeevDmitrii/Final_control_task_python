import csv
import os

class WorkWithCSV:

    __file_name = 'Notes.csv'

    def __init__(self, fields):
        self.__fields=fields

    def save_data_to_csv(self,notes_lst):
        with open(self.__file_name,'w',encoding='utf-8', newline='') as data_file_csv:
            writer = csv.DictWriter(data_file_csv, self.__fields, delimiter=';')
            writer.writeheader()
            writer.writerows(notes_lst)


    def read_data_from_csv(self):
        notes_lst = []
        if os.path.isfile(self.__file_name):
            with open(self.__file_name,'r',encoding='utf-8', newline='') as data_file_csv: 
                reader = csv.DictReader(data_file_csv, delimiter=';') 
                notes_lst=[i for i in reader]
        return notes_lst