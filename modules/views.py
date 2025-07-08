from modules import (get_task_summary)


def view_current_tasks(window):
    try:
        with open("files/todos.txt", "r") as local_file:
            all_tasks = local_file.readlines()
            current_summary = get_task_summary(all_tasks)
            if not current_summary:
                window["allTasksLabel"].update("No Current Outstanding "
                                               "Tasks", text_color="red")
                window["listOfTasks"].update([])
                return

            window["listOfTasks"].update(current_summary)
            window["allTasksLabel"].update("Current Outstanding Tasks")
    except FileNotFoundError:
        window["error"].update("No current tasks file found", visible=True)


def view_completed_tasks(window):
    try:
        with open("files/completed.txt", "r") as local_file:
            all_tasks = local_file.readlines()
            completed_summary = get_task_summary(all_tasks)
            if not completed_summary:
                window["allTasksLabel"].update("No Completed Tasks",
                                               text_color="red")
                window["listOfTasks"].update(values=[])
                return

            window["listOfTasks"].update(values=completed_summary)
            window["allTasksLabel"].update("Completed Tasks")
    except FileNotFoundError:
        window["error"].update("No completed tasks file found", visible=True)

