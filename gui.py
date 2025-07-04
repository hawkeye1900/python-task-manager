from modules import functions
import FreeSimpleGUI as sg
import time
import os

if not os.path.exists("todos.txt"):
    with open("todos.txt", "w") as file:
        pass

sg.theme("DarkGreen7")
clock = sg.Text("", key="clock")

# CREATE INPUT FIELDS AND LABELS
taskInputLabel = sg.Text("New task")
taskInputField = sg.InputText(tooltip="Enter new task", key="New task")

displaySelectedTaskLabel = sg.Text("Selected task")
displaySelectedTaskField = sg.InputText(tooltip="Display selected task",
                                        key="Selected task")

# CREATE BUTTONS
editBtn = sg.Button("Edit", key="Edit")
deleteBtn = sg.Button("Delete", key="Delete")
addTaskBtn = sg.Button("Add task", key="Add")
exitBtn = sg.Button("Exit", key="Exit")
completeBtn = sg.Button("Complete", key="Complete")
cancelBtn = sg.Button("Cancel", key="Cancel")


# DISPLAY TASKS
displayedTasks = sg.Listbox(values=functions.get_todos("r"),
                            key="listOfTasks",
                            enable_events=True,
                            size=(45, 12))

layout = [
    [clock],
    [taskInputLabel],
    [taskInputField, addTaskBtn],
    [displaySelectedTaskLabel, editBtn, completeBtn, deleteBtn],
    [displaySelectedTaskField],
    [displayedTasks],
    [exitBtn, cancelBtn]
]

# Create an instance of window class, with the title "Task Manager", and given
# layout and font
window = sg.Window("Task Manager", layout, font=("Helvetica", 20))


while True:
    event, values = window.read(timeout=1000,
                                close=False,
                                # if close=True, window closes after
                                # timeout
                                timeout_key="No new event")

    # The clock is updated every 1 second, due to the timeout value in read()
    # which is in ms
    window["clock"].update(value=time.strftime("%b %d, %Y %H:%M:%S"))

    match event:
        case "Add":
            tasksList = functions.get_todos("r")
            newTask = values["New task"]
            if not newTask:
                continue
            newTask = newTask + "\n"
            tasksList.append(newTask)
            print(tasksList)
            functions.get_todos("w", tasksList)
            window["New task"].update("")
            window["listOfTasks"].update(values=tasksList)
        case "Edit":
            try:
                # Select the task to be edited
                taskToEdit = values["listOfTasks"][0]

                # Enter new task
                newTask = values["New task"] + "\n"

                # Get tasklist from .txt
                tasksList = functions.get_todos("r")

                # Update tasklist list
                index = tasksList.index(taskToEdit)
                tasksList[index] = newTask
                functions.get_todos("w", tasksList)
                window["New task"].update("")
                window["listOfTasks"].update(values=tasksList)
            except IndexError:
                sg.popup("Please select a task first",
                         font=("Helvetica", 20))
        case "Delete":
            window["New task"].update("")
            print(values)
        case "Complete":
            try:
                tasksList = functions.get_todos("r")
                completedTask = values["listOfTasks"][0]
                tasksList.remove(completedTask)
                functions.get_todos("w", tasksList)
                window["listOfTasks"].update(values=tasksList)
                window["New task"].update("")
            except IndexError:
                sg.popup("Please select a task first",
                         font=("Helvetica", 20))
        case "Cancel":
            window["New task"].update("")
            continue
        case "listOfTasks":
            window["New task"].update(value=values["listOfTasks"][0]
                                      .strip("\n"))
        case sg.WIN_CLOSED:
            break
        case "Exit":
            break

window.close()
