from modules import (get_todos, add_task, edit_task, get_all_tasks,
                     delete_task, detailed_add, get_task_summary,
                     complete_task, view_current_tasks, view_completed_tasks)
import FreeSimpleGUI as sg
import time
import os

if not os.path.exists("files/todos.txt"):
    with open("files/todos.txt", "w") as file:
        pass

if not os.path.exists("files/completed.txt"):
    with open("files/completed.txt", "w") as file:
        pass

sg.theme("DarkGrey15")
clock = sg.Text("", key="clock", font=10)

# INPUT FIELDS AND LABELS
taskInputLabel = sg.Text("Add new task", font=14)
taskInputField = sg.InputText(tooltip="Add descriptive task title",
                              key="New task", font=14)
displayTaskView = sg.Text("Select View", font=14)
displaySelectedActionLabel = sg.Text("Select action", font=14)
tasksDisplayLabel = sg.Text("",
                            key="allTasksLabel",
                            text_color="red",
                            pad=((0, 0), (10, 0)),
                            font=14)
errorText = sg.Text(visible=False,
                    key="error",
                    background_color="red",
                    text_color="yellow",
                    pad=(10, 0),
                    font=14)

# BUTTONS
addTaskBtn = sg.Button("Quick Add",
                       key="Add",
                       bind_return_key=True,
                       font=12)
addDetailedTaskBtn = sg.Button("Detailed Add",
                               key="detailedAdd",
                               font=12)
editBtn = sg.Button("Edit", key="Edit", font=12)
viewCompletedTasksBtn = sg.Button("Completed",
                                  key="viewCompleted",
                                  font=12)
deleteBtn = sg.Button("Delete",
                      key="Delete",
                      font=12)
viewAllTasksBtn = sg.Button("All Tasks",
                            key="viewAll",
                            font=12)
viewOutstandingTasksBtn = sg.Button("Outstanding",
                                    key="viewCurrent",
                                    font=12)
completeBtn = sg.Button("Complete", key="Complete", font=12)
exitBtn = sg.Button("Exit", key="Exit", font=12)
cancelBtn = sg.Button("Cancel", key="Cancel", font=12)


# DISPLAY TASKS
tasksList = get_todos("r")
get_task_summary(tasksList)
displayedTasks = sg.Listbox(values=[],
                            key="listOfTasks",
                            enable_events=True,
                            size=(40, 8),
                            text_color="white",
                            pad=((0, 0), (5, 20)),
                            font=14
                            )

# ADD ELEMENTS TO LAYOUT
layout = [
    [clock],
    [taskInputLabel],
    [taskInputField, addTaskBtn],
    [displaySelectedActionLabel],
    [addDetailedTaskBtn, editBtn, completeBtn, deleteBtn],
    [displayTaskView],
    [errorText],
    [viewAllTasksBtn, viewOutstandingTasksBtn, viewCompletedTasksBtn],
    [tasksDisplayLabel],
    [displayedTasks],
    [exitBtn, cancelBtn]
]

# CREATE AN INSTANCE OF WINDOW CLASS AND ADD LAYOUT
main_window = sg.Window("Task Manager",
                        layout,
                        font=("Helvetica", 20),
                        finalize=True)

if not tasksList:
    tasksDisplayLabel.update("No Current Outstanding Tasks")
else:
    tasksDisplayLabel.update("Current Outstanding Tasks")
    displayedTasks.update(values=view_current_tasks(main_window))
while True:
    event, values = main_window.read(timeout=1000,
                                     close=False,
                                     timeout_key="No new event")

    # The clock is updated every 1 second, due to the timeout value in read()
    main_window["clock"].update(value=time.strftime("%b %d, %Y %H:%M:%S"))

    match event:
        case "Add":
            add_task(values, main_window)
        case "detailedAdd":
            detailed_add(main_window)
        case "Edit":
            edit_task(main_window)
        case "Delete":
            delete_task(main_window)
        case "Complete":
            try:
                all_completed_tasks = complete_task("r")
                all_tasks = get_todos("r")
                completedTask = values["listOfTasks"][0]
                index_of_task = all_tasks.index(completedTask)

                all_tasks.remove((all_tasks[index_of_task]))
                all_completed_tasks.append(completedTask)

                get_todos("w", all_tasks)
                complete_task("w", all_completed_tasks)

                main_window["listOfTasks"].update(values=get_task_summary(
                    all_tasks))
                main_window["New task"].update("")
            except IndexError:
                sg.popup("Please select a task first",
                         font=("Helvetica", 20))
                continue
        case "viewAll":
            # get_all_tasks(displayedTasks)
            displayedTasks.update(values=get_task_summary(get_all_tasks()))
            tasksDisplayLabel.update("All Tasks")
        case "viewCurrent":
            view_current_tasks(main_window)
        case "viewCompleted":
            view_completed_tasks(main_window)
        case "Cancel":
            main_window["New task"].update("")
            main_window["error"].update(visible=False)
            view_current_tasks(main_window)
            continue
        case sg.WIN_CLOSED:
            break
        case "Exit":
            break

main_window.close()
