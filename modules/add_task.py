import FreeSimpleGUI as sg
from modules import (get_outstanding_todos, get_task_summary)


def add_task(values, window):
    new_task = values["New task"]
    if not new_task:
        return
    if "\n" in new_task:
        sg.popup("You entered an invalid character - \\n")
        values["New task"] = ""

    task = new_task + "\n"
    tasks_list = get_outstanding_todos("r")
    tasks_list.append(task)
    get_outstanding_todos("w", tasks_list)
    print(tasks_list)

    window["New task"].update("")
    window["listOfTasks"].update(values=get_task_summary(tasks_list))
    window["allTasksLabel"].update("Current Outstanding Tasks",
                                   text_color="red")
