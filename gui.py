from modules import functions
import FreeSimpleGUI as fsg
import time
import os

if not os.path.exists("todos.txt"):
    with open("todos.txt", "w") as file:
        pass

fsg.theme("DarkGreen7")
clock = fsg.Text("", key="clock")

# INPUT FIELDS AND LABELS
# Input label followed by field which returns a dictionary with key
# (ie "New Task") as the dictionary key value, and the input is returned
# as the value. It is the key that window uses to refer to that element and
# get the value

taskInputLabel = fsg.Text("New task")
taskInputField = fsg.InputText(tooltip="Enter new task",
                               key="New task")

displaySelectedTaskLabel = fsg.Text("Selected task")
displaySelectedTaskField = fsg.InputText(tooltip="Display selected task",
                                         key="Selected task")

# CREATE BUTTONS - by default they return a click event. Events can be disabled
editBtn = fsg.Button("Edit", key="Edit")
deleteBtn = fsg.Button("Delete", key="Delete")
addTaskBtn = fsg.Button("Add task", key="Add")
exitBtn = fsg.Button("Exit", key="Exit")
completeBtn = fsg.Button("Complete", key="Complete")
cancelBtn = fsg.Button("Cancel", key="Cancel")


# DISPLAY FIELDS
displayedTasks = fsg.Listbox(values=functions.get_todos("r"),
                             key="listOfTasks",
                             enable_events=True,
                             size=(45, 12))

layout = [
    [clock],
    [taskInputLabel],
    [taskInputField, addTaskBtn],
    [editBtn, completeBtn, deleteBtn],
    [displaySelectedTaskLabel],
    [displaySelectedTaskField],
    [displayedTasks],
    [exitBtn, cancelBtn]
]

# Create an instance of window class, with the title "Task Manager", and given
# layout and font
window = fsg.Window("Task Manager",
                    layout,
                    font=("Helvetica", 20))


while True:
    # window.read() reads data from window events.
    # the timeout param causes read to wait for user interaction. If no
    # interaction takes place, it returns a timeout_key
    # the read() call returns 2 values, by convention known as event, values

    # In all windows, events are triggered by:
    #
    # Button click
    # Window closed using X

    # Other events can be specifcally enabled using 'enable_events=True'
    # when an element is created.

    event, values = window.read(timeout=1000,
                                close=False,
                                # if close=True, window closes after
                                # timeout
                                timeout_key="No new event")

    # The clock is updated every 1 second, due to the timeout value in read()
    # which is in ms
    window["clock"].update(value=time.strftime("%b %d, %Y %H:%M:%S"))

    #   The event returns the key text from the button pressed or input
    #   changed, ie if addTaskBtn is pressed, event = "Add"

    #   values is a list or as in this case a dictionary of inputs,
    #   where each input has a key and is given a value, which makes up the
    #   dictionary key:value pairs. If the task input field receives a
    #   value, then its key is "New task", which will be the key in the
    #   dictionary key/value pair. Its value then is the value in the dict.

    match event:
        case "Add":
            tasksList = functions.get_todos("r")
            newTask = values["New task"]
            if not newTask:
                continue
            newTask = newTask + "\n"
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
            except IndexError:
                fsg.popup("Please select a task first",
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
                fsg.popup("Please select a task first",
                          font=("Helvetica", 20))
        case "Cancel":
            window["New task"].update("")
            continue
        case "listOfTasks":
            window["New task"].update(value=values["listOfTasks"][0]
                                      .strip("\n"))
        case fsg.WIN_CLOSED:
            break
        case "Exit":
            break


window.close()
