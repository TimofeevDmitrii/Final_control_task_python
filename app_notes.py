from all_menu_operations import AllMenuOperations
from all_menu_operations import ControllerNotes
from auxilary import NotesColumnsView



controller = ControllerNotes(AllMenuOperations(), NotesColumnsView()) 
controller.start_working_proccess()
