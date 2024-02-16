import csv
import os
import datetime
import abc



class NotesMenu:

    def show_menu(self):
        print('1. Распечатать все заметки',
            '2. Добавить новую заметку',
            '3. Редактировать заметку',
            '4. Найти заметку(и) по дате создания',
            '5. Найти заметку(и) по дате изменения',
            '6. Найти заметку по id',
            '7. Удалить заметку',
            '8. Закончить работу', sep = '\n')
        return self.__input_choice()

    def show_find_menu(self):
        print('1. Определить заметку(и) по дате создания',
            '2. Определить заметку(и) по дате изменения',
            '3. Определить заметку по id',
            '4. Вернуться к главному меню', sep = '\n') 
        return self.__input_choice()

    
    def show_edit_menu(self):
        print('1. Изменить название заметки',
            '2. Изменить описание заметки',
            '3. Отменить изменения и вернуться к главному меню',
            '4. Сохранить изменения и вернуться к главному меню', sep = '\n') 
        return self.__input_choice()

    def __input_choice(self):
        try:
            return int(input("--->Введите номер команды из списка:\n--->"))
        except ValueError:
            print("--->Неверный ввод команды - ожидается целое положительное число (номер команды из списка)")
            return 0





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



class NotesConsoleView(abc.ABC):

    @abc.abstractmethod
    def print_notes(self, notes_lst):
        pass



class StandartNotesView(NotesConsoleView):

    def print_notes(self, notes_lst):
        for i in notes_lst:
            for k,v in i.items():
                print(k+':'+v)
            print('\n')



class NotesColumnsView(NotesConsoleView):

    __fields=['id','Дата создания','Дата изменения','Название заметки','Описание заметки'] 
    __column_sizes={'id': 8, 'Дата создания': 20, 'Дата изменения': 20, 'Название заметки': 40, 'Описание заметки':50}


    
    def print_notes(self, notes_lst):
        correct_size_for_print=lambda x,n:x+''.join([' ' for i in range(n-len(x))]) # функция добавляет недостающее количество пробелов до фиксированного размера n
        
        for k in self.__fields:
            print(correct_size_for_print(k,self.__column_sizes[k]),end='')
        print()
        for i in notes_lst:
            for k,v in i.items():
                if k=='Описание заметки' and len(v)>self.__column_sizes[k]-1:
                    self.__print_long_description(v)
                else:
                    print(correct_size_for_print(v,self.__column_sizes[k]-1),end=' ')
            print('\n')


    def __count_spaces_num(self,key):
        spaces_number=0
        for i in self.__fields:
            if i==key:
                break
            else:
                spaces_number+=self.__column_sizes[i]
        return spaces_number

    def __print_long_description(self, descr):
        count=1
        for i in range(len(descr)):
            if (i!=(self.__column_sizes['Описание заметки']-1)*count):
                print(descr[i], end='')
            else:
                print(' ')
                print(''.join([' ']*self.__count_spaces_num('Описание заметки')), end='')
                print(descr[i], end='')
                count+=1




class WorkWithNotes:

    
    __fields=['id','Дата создания','Дата изменения', 'Название заметки', 'Описание заметки']
    __data_csv=WorkWithCSV(__fields)

    def __init__(self, view=StandartNotesView):
        self.__view_notes=view


    def read_data_notes(self):
        return self.__data_csv.read_data_from_csv()

    
    def save_data_notes(self, all_notes):
         self.__data_csv.save_data_to_csv(all_notes)


    def give_id_to_new_note(self, all_notes):
        if len(all_notes)!=0:
            return str(max([int(i['id']) for i in all_notes])+1)
        else:
            return '1'


    def get_correct_data(self, curr_note, curr_key):
        letter_symbols=[chr(i) for i in range(1040,1104)]+[chr(i) for i in range(65,91)]+[chr(i) for i in range(97,123)] # все буквенные символы кириллицы и латиницы
        correct_data=False
        while not correct_data:
            curr_note[curr_key]=input(f'--->Введите данные для поля "{curr_key}":\n--->').strip().replace(';','.') # если вдруг попала ';' в поле, то будем ее менять на точку, иначе может взникнуть проблема при распаковке данных программой
            if set(curr_note[curr_key])&set(letter_symbols)==set():                                # из csv файла, т.к. разделителем принят ';'(на этот случай есть отстройка в DictWriter (заключает данные, содержащие ';' в ковычки), но возможно это есть не во всех версиях)
                print(f'--->Поле "{curr_key}" обязательно для заполнения и должно содержать буквенные символы')
            else:
                correct_data=True 


    def find_note_index(self, all_notes, id): 
        for i in range(len(all_notes)):
            if all_notes[i]['id']==id:
                return i
        else:
            return '--->Заметки с таким id нет'



    def find_notes_indexes_by_date_range(self,all_notes, date_key):
        print("--->Укажите границы диапазона поиска по "+date_key.replace('Дата','дате'))
        try:
            start_date=datetime.datetime.strptime(input('--->Введите начальную дату поиска (формат ввода - дд.мм.гггг; например, 01.08.2022):\n--->').strip(), '%d.%m.%Y')
            end_date=datetime.datetime.strptime(input('--->Введите конечную дату поиска (формат ввода - дд.мм.гггг; например, 01.08.2022):\n--->').strip(), '%d.%m.%Y')
        except ValueError:
            return "--->При вводе даты использован неверный формат"
        if (start_date>end_date):
            return "--->Внимание: была указана начальная дата, которая позже конечной даты"
        filter_date_range=lambda check_date: start_date<=check_date and end_date>=check_date
        return [i for i in range(len(all_notes)) if filter_date_range(datetime.datetime.strptime(all_notes[i][date_key].split('/')[0], '%d.%m.%Y'))]



    def find_note_index_for_change(self, all_notes, start_search_param):
        result_index_for_edit=''
        search_params={1: 'Дата создания', 2:'Дата изменения', 3: 'id'}
        if (start_search_param in [1,2]):
            find_index_lst=self.find_notes_indexes_by_date_range(all_notes, search_params[start_search_param])
            if (type(find_index_lst)!=str):
                if (len(find_index_lst)==0):
                    result_index_for_edit="--->Не найдено заметок, удовлетворяющих запрос по дате"
                elif (len(find_index_lst)==1):
                    result_index_for_edit=self.find_note_index(all_notes, all_notes[find_index_lst[0]]['id'])
                else:
                    find_notes=[all_notes[i] for i in find_index_lst]
                    self.__view_notes.print_notes(find_notes)
                    message="--->Найдено несколько заметок с подходящей "+ search_params[start_search_param].replace('Дата','датой')+'\n--->Уточните id искомой заметки в списке отобранных заметок:\n--->'
                    id_for_search=input(message)
                    if (id_for_search in [i['id'] for i in find_notes]):
                        result_index_for_edit=self.find_note_index(all_notes, id_for_search)
                    else:
                        result_index_for_edit="--->Не найдено заметок с таким id в отобранном списке"
            else:
                result_index_for_edit=find_index_lst
        else:
            result_index_for_edit=self.find_note_index(all_notes, input("--->Ввeдите id заметки для поиска:\n--->"))
        return result_index_for_edit