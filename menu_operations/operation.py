import abc
from auxilary.work_with_notes import WorkWithNotes
from auxilary.notes_view import NotesView
from auxilary.work_with_csv import WorkWithCSV

class Operation(abc.ABC):

    def __init__(self):
        self.work_tools=WorkWithNotes()
        self.view_tools=NotesView()
        self.csv_tools=WorkWithCSV()

    @abc.abstractmethod
    def make_operation(self):
        pass
