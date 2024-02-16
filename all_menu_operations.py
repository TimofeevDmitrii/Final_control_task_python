import abc
from auxilary import WorkWithNotes
from auxilary import NotesConsoleView
from auxilary import StandartNotesView
from auxilary import NotesMenu
import datetime
import traceback

class MenuOperationsNotes(abc.ABC):

    @abc.abstractmethod
    def get_operation(self, number):
        pass

    @abc.abstractmethod
    def contains_key(self, number):
        pass


class ControllerNotes:


    def __init__(self, operations: MenuOperationsNotes, view=StandartNotesView()):
        self.__using_operation=operations
        self.__using_operation.initialize(view)
        self.__menu=NotesMenu()

    def start_working_proccess(self):
        try:
            all_notes_list=WorkWithNotes().read_data_notes()
            choice=self.__menu.show_menu()
            while (choice!=8):
                if (self.__using_operation.contains_key(choice)):
                    curr_operation=self.__using_operation.get_operation(choice)
                    curr_operation.make(all_notes_list)
                print()
                choice= self.__menu.show_menu()
        except Exception as e:
            print("\n--->В ходе работы программы произошла ошибка. Возможно файл Notes.csv был поврежден")
            print("--->Завершение работы.")
            print(e, traceback.format_exc())


class AllMenuOperations(MenuOperationsNotes):

    def initialize(self, view: NotesConsoleView):
        self.__all_operations={1: PrintAllNotes(view),
                             2: AddNote(view),
                             3: EditNote(view),
                             4: FindNoteByCreateDate(view),
                             5: FindNoteByEditDate(view),
                             6: FindNoteById(view),
                             7: DeleteNote(view)}

    def get_operation(self, number):
        return self.__all_operations[number]
    
    def contains_key(self, number):
        return number in self.__all_operations.keys()


class Operation(abc.ABC):

    def __init__(self, view=StandartNotesView()):
        self.work_tools=WorkWithNotes(view)
        self.view_tools=view

    @abc.abstractmethod
    def make(self):
        pass



class PrintAllNotes(Operation):

    def make(self, all_notes):
        if (len(all_notes)==0):
            print("--->Еще не было создано ни одной заметки")
        else:
            self.view_tools.print_notes(all_notes)



class AddNote(Operation):

    def make(self, all_notes):
        new_note={}
        new_note['id']=self.work_tools.give_id_to_new_note(all_notes)

        current_date = datetime.datetime.today().strftime('%d.%m.%Y/%H:%M')
        new_note['Дата создания']=current_date
        new_note['Дата изменения']=current_date

        for i in 'Название заметки','Описание заметки':
            self.work_tools.get_correct_data(new_note,i) 
        if (len(new_note['Название заметки'])>39):
            new_note['Название заметки']=new_note['Название заметки'][:39]  
        all_notes.append(new_note)
        self.work_tools.save_data_notes(all_notes)
        print(f'--->Добавлена новая заметка (id: {new_note["id"]})')


class EditNote(Operation):

    def make(self, all_notes):
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
                        self.work_tools.get_correct_data(edit_note, edit_fields[edit_choice-1])
                        edit=True
                    edit_choice=menu.show_edit_menu()
                if(edit_choice==4 and edit==True): 
                    if (len(edit_note['Название заметки'])>39):
                        edit_note['Название заметки']=edit_note['Название заметки'][:39]
                    print("--->Заметка изменена")
                    edit_note['Дата изменения']=datetime.datetime.today().strftime('%d.%m.%Y/%H:%M')
                    all_notes[note_index_for_edit]=edit_note
                    self.view_tools.print_notes([all_notes[note_index_for_edit]])
                    self.work_tools.save_data_notes(all_notes)
                    print("--->Изменения сохранены")




class FindNoteByCreateDate(Operation):

     def make(self, all_notes):
        find_note_indexes=self.work_tools.find_notes_indexes_by_date_range(all_notes, 'Дата создания')
        if type(find_note_indexes)==str:
            print(find_note_indexes) 
        else:
            if(len(find_note_indexes)!=0):
                self.view_tools.print_notes([all_notes[i] for i in find_note_indexes])
            else:
                print("--->Нет заметок из указанного диапазона дат создания")


class FindNoteByEditDate(Operation):

     def make(self, all_notes):
        find_note_indexes=self.work_tools.find_notes_indexes_by_date_range(all_notes, 'Дата изменения')
        if type(find_note_indexes)==str:
            print(find_note_indexes) 
        else:
            if(len(find_note_indexes)!=0):
                self.view_tools.print_notes([all_notes[i] for i in find_note_indexes])
            else:
                print("--->Нет заметок из указанного диапазона дат изменения")



class FindNoteById(Operation):

     def make(self, all_notes):
        note_index=self.work_tools.find_note_index(all_notes, input("--->Введите id для поиска:\n--->"))
        if type(note_index)==str:
            print(note_index) 
        else:
            self.view_tools.print_notes([all_notes[note_index]])



class DeleteNote(Operation):

    def make(self, all_notes):
        menu=NotesMenu()
        find_choice=menu.show_find_menu()
        while(find_choice not in range(1,5)):
            find_choice=menu.show_find_menu()
        if (find_choice!=4):
            note_index_for_delete=self.work_tools.find_note_index_for_change(all_notes,find_choice)
            if(type(note_index_for_delete)==str):
                print(note_index_for_delete)
            else:
                self.view_tools.print_notes([all_notes[note_index_for_delete]])
                delete=''
                while delete not in ['yes','no']:
                    delete=input("--->Подтвердите удаление данной заметки - напечатайте yes или no:\n--->")
                if delete=='yes':
                    all_notes.pop(note_index_for_delete)
                    self.work_tools.save_data_notes(all_notes)
                    print("--->Данная заметка удалена\n")