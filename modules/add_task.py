import FreeSimpleGUI as sg
from .get_todos import get_todos


def add_task(values, window):
    new_task = values["New task"]
    if not new_task:
        print("Invalid")
        return
    if "\n" in new_task:
        sg.popup("You entered an invalid character - \\n")
        values["New task"] = ""

    task = new_task + "\n"
    tasks_list = get_todos("r")
    tasks_list.append(task)
    get_todos("w", tasks_list)

    window["New task"].update("")
    window["listOfTasks"].update(values=tasks_list)