from modules import functions
import FreeSimpleGUI as fsg
import time
import os

if not os.path.exists("todos.txt"):
    with open("todos.txt", "w") as file:
        pass

fsg.theme("DarkGreen5")


# INPUT FIELDS AND LABELS
# Input label followed by field which returns a dictionary with key (ie "New Task") as the dictionary
# key value, and the input is returned as the value
clock = fsg.Text("", key="clock")
taskInputLabel = fsg.Text("Enter task:")
taskInputField = fsg.InputText(tooltip="Enter new task",
                               key="New task")


# BUTTONS
editBtn = fsg.Button("Edit")
# deleteBtn = fsg.Button("Delete")
addTaskBtn = fsg.Button("Add task", key="Add")
exitBtn = fsg.Button("Exit")
completeBtn = fsg.Button("Complete")
cancelBtn = fsg.Button("Cancel")


# DISPLAY FIELDS
displayedTasks = fsg.Listbox(values=functions.get_todos("r"),
                             key="listOfTasks",
                             enable_events=True,
                             size=(45, 12))


layout = [
    [clock],
    [taskInputLabel],
    [taskInputField, addTaskBtn],
    [displayedTasks, editBtn, completeBtn],
    [exitBtn, cancelBtn]
]

# Create an instance of window type, with the title "Task Manager", and given layout and font
window = fsg.Window("Task Manager",
                    layout,
                    font=("Helvetica", 20))



while True:
    # window.read() pauses the program and waits for user interaction
    # the event return value can be de-structured
    # and the event used to decide on the next step
    event, values = window.read(timeout=1000)
    window["clock"].update(value=time.strftime("%b %d, %Y %H:%M:%S"))
    # The event returns a tuple containing:
    #   the text from the button pressed (the event), ie if addTaskBtn is pressed, ("Add task", {})
    #   followed by a dictionary with key set to the input field key
    #   and the value is the string entered into the input field

    match event:
        case "Add":
            tasksList = functions.get_todos("r")
            newTask = values["New task"] + "\n"
            tasksList.append(newTask)
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
                print("Print tasklist", tasksList)
            except IndexError:
                fsg.popup("Please select a task first",
                          font=("Helvetica", 20))
        case "Complete":
            try:
                tasksList = functions.get_todos("r")
                completedTask = values["listOfTasks"][0]
                tasksList.remove(completedTask)
                functions.get_todos("w", tasksList)
                window["listOfTasks"].update(values=tasksList)
                window["New task"].update("")
            except IndexError:
                fsg.popup("Please select a task first",
                          font=("Helvetica", 20))
        case "Cancel":
            window["New task"].update("")
            continue
        case "listOfTasks":
            window["New task"].update(value=values["listOfTasks"][0].strip("\n"))
        case fsg.WIN_CLOSED:
            break
        case "Exit":
            break


window.close()
