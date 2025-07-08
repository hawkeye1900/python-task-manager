import FreeSimpleGUI as sg

from modules import (get_todos, get_task_summary)


def edit_task(window):
    try:
        all_tasks = get_todos("r")
        layout = [
            [sg.Text("Task for editing", size=(12, 1), font=14),
             sg.InputText(key="edit_task", font=14)],
            [sg.Listbox(values=all_tasks,
                        key="listOfTasks",
                        size=(45, 8),
                        text_color="white",
                        enable_events=True,
                        font=14)],
            [sg.Exit(font=12), sg.Save(font=12), sg.Cancel(font=12)]
        ]

        edit_window = sg.Window("Edit Window",
                               layout,
                               font=("Helvetica", 20))

        while True:
            event, values = edit_window.read()

            match event:
                case "listOfTasks":
                    if values["listOfTasks"]:
                        (edit_window["edit_task"]
                         .update(value=values["listOfTasks"][0].strip("\n")))

                case "Save":
                    task_to_be_edited = values["listOfTasks"][0]
                    index_of_task = all_tasks.index(task_to_be_edited)

                    if values["edit_task"]:
                        if "\n" in values["edit_task"]:
                            all_tasks.remove(all_tasks[index_of_task])
                        else:
                            edited_task = values["edit_task"]
                            all_tasks[index_of_task] = edited_task + "\n"
                    else:
                        all_tasks.remove(all_tasks[index_of_task])

                    get_todos("w", all_tasks)
                    edit_window["edit_task"].update("")
                    edit_window["listOfTasks"].update(
                        values=get_task_summary(all_tasks))
                    window["listOfTasks"].update(
                        values=get_task_summary(all_tasks))
                    continue
                case "Cancel":
                    edit_window["edit_task"].update("")
                    continue
                case sg.WIN_CLOSED:
                    break
                case "Exit":
                    break
        edit_window.close()
    except IndexError:
        pass