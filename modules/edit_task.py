import FreeSimpleGUI as sg
from .get_todos import get_todos


def edit_task():
    try:
        all_tasks = get_todos("r")
        layout = [
            [sg.Text("Task for editing", size=(12, 1)),
             sg.InputText(key="edit_task")],
            [sg.Listbox(values=all_tasks,
                        key="listOfTasks",
                        size=(45, 8),
                        text_color="white",
                        enable_events=True)],
            [sg.Exit(), sg.Save(), sg.Cancel()]
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
                    # Get tasks array index of task being edited
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
                    edit_window["listOfTasks"].update(values=all_tasks)
                    continue
                case "Cancel":
                    edit_window["edit_task"].update("")
                case sg.WIN_CLOSED:
                    break
                case "Exit":
                    break
        edit_window.close()
    except IndexError:
        pass