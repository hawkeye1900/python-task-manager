from modules import (get_todos, add_task, detailed_add, edit_task,
                     delete_task, complete_task)
import FreeSimpleGUI as sg
import time
import os

if not os.path.exists("todos.txt"):
    with open("todos.txt", "w") as file:
        pass

sg.theme("DarkGrey15")
clock = sg.Text("", key="clock")

# CREATE INPUT FIELDS AND LABELS
taskInputLabel = sg.Text("New task")
taskInputField = sg.InputText(tooltip="Enter new task", key="New task")
displaySelectedTaskLabel = sg.Text("Select action:")
allTasksLabel = sg.Text("Tasks", pad=((0, 0), (10, 0)))

# CREATE BUTTONS
editBtn = sg.Button("Edit", key="Edit")
deleteBtn = sg.Button("Delete", key="Delete")
addTaskBtn = sg.Button("Quick Add", key="Add", bind_return_key=True)
addDetailedTaskBtn = sg.Button("Detailed Add", key="detailedAdd")
exitBtn = sg.Button("Exit", key="Exit")
completeBtn = sg.Button("Complete", key="Complete")
cancelBtn = sg.Button("Cancel", key="Cancel")


# DISPLAY TASKS
tasksList = get_todos("r")
displayedTasks = sg.Listbox(values=tasksList,
                            key="listOfTasks",
                            enable_events=True,
                            size=(45, 8),
                            text_color="white",
                            pad=((0, 0), (5, 20))
                            )

# ADD ELEMENTS TO LAYOUT
layout = [
    [clock],
    [taskInputLabel],
    [taskInputField, addTaskBtn],
    [displaySelectedTaskLabel],
    [addDetailedTaskBtn, editBtn, completeBtn, deleteBtn],
    [allTasksLabel],
    [displayedTasks],
    [exitBtn, cancelBtn]
]

# CREATE AN INSTANCE OF WINDOW CLASS AND ADD LAYOUT
window = sg.Window("Task Manager", layout, font=("Helvetica", 20))


while True:
    event, values = window.read(timeout=1000,
                                close=False,
                                timeout_key="No new event")

    # The clock is updated every 1 second, due to the timeout value in read()
    window["clock"].update(value=time.strftime("%b %d, %Y %H:%M:%S"))

    match event:
        case "Add":
            tasksList = add_task(values, window)
            window["listOfTasks"].update(values=tasksList)
        case "detailedAdd":
            detailed_add()
        case "Edit":
            edit_task()
            tasksList = get_todos("r")
            window["listOfTasks"].update(values=tasksList)
        case "Delete":
            delete_task()
            tasksList = get_todos("r")
            window["listOfTasks"].update(values=tasksList)
        case "Complete":
            try:
                tasksList = get_todos("r")
                completedTask = values["listOfTasks"][0]
                tasksList.remove(completedTask)
                get_todos("w", tasksList)
                window["listOfTasks"].update(values=tasksList)
                window["New task"].update("")
            except IndexError:
                sg.popup("Please select a task first",
                         font=("Helvetica", 20))
        case "Cancel":
            window["New task"].update("")
            continue
        case sg.WIN_CLOSED:
            break
        case "Exit":
            break

window.close()
