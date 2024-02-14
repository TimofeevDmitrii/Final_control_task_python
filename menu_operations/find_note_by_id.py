import operation

class FindNoteById(operation.Operation):

     def find_note_by_id(self, all_notes): 
        note_index=self.work_tools.find_note_index(all_notes, input("Введите id для поиска:"))
        if type(note_index)==str:
            print(note_index) 
        else:
            self.view_tools.print_notes([all_notes[note_index]])