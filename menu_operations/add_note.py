import operation
import datetime

class AddNote(operation.Operation):

    def make_operation(self, all_notes):
        new_note={}
        new_note['id']=self.work_tools.give_id_to_new_note(all_notes)

        current_date = datetime.date.today().strftime('%d.%m.%Y')
        new_note['Дата создания']=current_date
        new_note['Дата изменения']=current_date

        for i in 'Название заметки','Описание заметки':
            self.work_tools.get_correct_data(new_note,i) 
        if (len(new_note['Название заметки'])>39):
            new_note['Название заметки']=new_note['Название заметки'][:39]  
        all_notes.append(new_note)
        self.csv_tools.save_data_to_csv(all_notes)
        print(f'Добавлена новая заметка (id: {new_note["id"]})')