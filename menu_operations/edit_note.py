import operation
import datetime
from auxilary.menu_notes import NotesMenu

class EditNote(operation.Operation):

    def make_operation(self, all_notes):
        menu=NotesMenu()
        find_choice=menu.show_find_menu()
        while(find_choice not in range(1,5)):
            find_choice=menu.show_find_menu()
        if (find_choice!=4):
            note_index_for_edit=self.work_tools.find_note_index_for_change(all_notes,find_choice)
            if(type(note_index_for_edit)==str):
                print(note_index_for_edit)
            else:
                edit=False
                edit_note=all_notes[note_index_for_edit].copy()
                self.view_tools.print_notes([all_notes[note_index_for_edit]])
                edit_choice=menu.show_edit_menu()
                while(edit_choice not in [3,4]):
                    if (edit_choice in [1,2]):
                        edit_fields=['Название заметки','Описание заметки']
                        self.work_tools.get_correct_data(edit_note, edit_fields[edit_choice])
                        edit=True
                    edit_choice=menu.show_edit_menu()
                if(edit_choice==4 and edit==True): 
                    print("Заметка изменена")
                    edit_note['Дата изменения']=datetime.date.today().strftime('%d.%m.%Y')
                    all_notes[note_index_for_edit]=edit_note
                    self.view_tools.print_notes([all_notes[note_index_for_edit]])
                    self.csv_tools.save_data_to_csv(all_notes)