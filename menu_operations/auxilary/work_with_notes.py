import datetime
import notes_view

class WorkWithNotes:

    __fields=['id','Дата создания','Дата изменения','Название заметки','Описание заметки']
    __view_notes=notes_view.NotesView() 
    

    def give_id_to_new_note(self, all_notes):
        if len(all_notes)!=0:
            return str(max([int(i['id']) for i in all_notes])+1)
        else:
            return '1'


    def get_correct_data(self, curr_note, curr_key):
        letter_symbols=[chr(i) for i in range(1040,1104)]+[chr(i) for i in range(65,91)]+[chr(i) for i in range(97,123)] # все буквенные символы кириллицы и латиницы
        correct_data=False
        while not correct_data:
            curr_note[curr_key]=input(f'Введите данные для поля "{curr_key}": ').strip().replace(';','.') # если вдруг попала ';' в поле, то будем ее менять на точку, иначе может взникнуть проблема при распаковке данных программой
            if set(curr_note[curr_key])&set(letter_symbols)==set():                                # из csv файла, т.к. разделителем принят ';'(на этот случай есть отстройка в DictWriter (заключает данные, содержащие ';' в ковычки), но возможно это есть не во всех версиях)
                print(f'Поле "{curr_key}" обязательно для заполнения и должно содержать буквенные символы')
            else:
                correct_data=True 


    def find_note_index(self, all_notes, id): 
        for i in range(len(all_notes)):
            if all_notes[i]['id']==id:
                return i
        else:
            return 'Заметки с таким id нет'


    def find_notes_by_date(self, all_notes, date_key):  
        try:
            date=datetime.datetime.strptime(input('Введите '+date_key.replace('Дата','дату')+':'), '%d.%m.%Y')
        except ValueError:
            print("При вводе даты использован неверный формат")
            return []
        return list(filter(lambda x: date==datetime.datetime.strptime(x[date_key], '%d.%m.%Y'), all_notes))


    def find_note_index_for_change(self, all_notes, start_search_param):
        result_index_for_edit=''
        search_params={1: 'Дата создания', 2:'Дата изменения', 3: 'id'}
        if (start_search_param in [1,2]):
            find_lst=self.find_notes_by_date(all_notes, search_params[start_search_param])
            if (len(find_lst)==0):
                result_index_for_edit="Не найдено заметок с такой датой или возникла ошибка при вводе даты поиска"
            elif (len(find_lst)==1):
                result_index_for_edit=self.find_note_index(all_notes, find_lst[0]['id'])
            else:
                self.__view_notes.print_notes(find_lst)
                message="Найдено несколько заметок с такой "+ search_params[start_search_param].replace('Дата','датой')+';\nВведите дополнительно id для поиска:'
                result_index_for_edit=self.find_note_index(all_notes, input(message))
        else:
            result_index_for_edit=self.find_note_index(all_notes, input("Ввeдите id заметки для поиска"))
        return result_index_for_edit


        
