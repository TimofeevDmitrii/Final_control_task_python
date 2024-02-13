import datetime

class WorkWithNotes:

    __fields=['id','Дата создания','Дата изменения','Название заметки','Описание заметки'] 
    

    def __give_id_to_new_note(self, notes_lst):
        if len(notes_lst)!=0:
            return str(max([int(i['id']) for i in notes_lst])+1)
        else:
            return '1'

    

    def add_new_note(self, notes_lst):
        new_note={}
        letter_symbols=[chr(i) for i in range(1040,1104)]+[chr(i) for i in range(65,91)]+[chr(i) for i in range(97,123)] # все буквенные символы кириллицы и латиницы
        new_note['id']=self.__give_id_to_new_note(notes_lst)

        current_date = datetime.date.today().strftime('%d.%m.%Y')
        new_note['Дата создания']=current_date
        new_note['Дата изменения']=current_date

        for i in 'Название заметки','Описание заметки':
            correct_data=False
            while not correct_data:
                new_note[i]=input(f'Введите данные для поля "{i}": ').strip().replace(';','.') # если вдруг попала ';' в поле, то будем ее менять на точку, иначе может взникнуть проблема при распаковке данных программой
                if set(new_note[i])&set(letter_symbols)==set():                                # из csv файла, т.к. разделителем принят ';'(на этот случай есть отстройка в DictWriter (заключает данные, содержащие ';' в ковычки), но возможно это есть не во всех версиях)
                    print(f'Поле "{i}" обязательно для заполнения и должно содержать буквенные символы')
                else:
                    correct_data=True 
        if (len(new_note['Название заметки'])>39):
            new_note['Название заметки']=new_note['Название заметки'][:39]  
        notes_lst.append(new_note)
        print(f'Добавлена новая заметка (id: {new_note["id"]})')


    def __find_note_index(self, notes_lst, id): 
        for i in range(len(notes_lst)):
            if notes_lst[i]['id']==id:
                return i
        else:
            return 'Заметки с таким id нет'

    
    def find_note_by_id(self, notes_lst): 
        note_index=self.__find_note_index(notes_lst, input("Введите id для поиска:"))
        if type(note_index)==str:
            print(note_index) 
            return []
        else:
            return [notes_lst[note_index]]

    def find_notes_by_date(self, notes_lst, date_key):  
        try:
            date=datetime.datetime.strptime(input('Введите '+date_key.replace('Дата','дату')+':'), '%d.%m.%Y')
        except ValueError:
            print("При вводе даты использован неверный формат")
            return []
        return list(filter(lambda x: date==datetime.datetime.strptime(x[date_key], '%d.%m.%Y'), notes_lst))

    # def find_note_for_edit(notes_lst):
        
