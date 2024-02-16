from all_menu_operations import AllMenuOperations
from all_menu_operations import ControllerNotes
from auxilary import NotesView



controller = ControllerNotes(AllMenuOperations(), NotesView())
controller.start_working_proccess()
