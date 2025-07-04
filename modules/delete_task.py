from .get_todos import get_todos
import FreeSimpleGUI as sg


def delete_task():
    try:
        all_tasks = get_todos("r")
        layout = [
            [sg.InputText(key="delete_task")],
            [sg.Button("Delete task?", key="Delete")],
            [sg.Listbox(values=all_tasks,
                        key="listOfTasks",
                        size=(45, 8),
                        text_color="white",
                        enable_events=True)],
            [sg.Exit(), sg.Cancel()]
        ]

        delete_window = sg.Window("Delete Window",
                                  layout,
                                  font=("Helvetica", 20))

        while True:
            event, values = delete_window.read()

            match event:
                case "listOfTasks":
                    if values["listOfTasks"]:
                        (delete_window["delete_task"]
                         .update(value=values["listOfTasks"][0].strip("\n")))

                case "Delete":
                    choice = sg.popup_ok_cancel("Confirm OK? Cancel")
                    if choice == "OK":
                        task_to_be_deleted = values["listOfTasks"][0]
                        index_of_task = all_tasks.index(task_to_be_deleted)
                        all_tasks.remove(all_tasks[index_of_task])

                        get_todos("w", all_tasks)
                        delete_window["delete_task"].update("")
                        delete_window["listOfTasks"].update(values=all_tasks)
                    else:
                        continue
                case "Cancel":
                    delete_window["delete_task"].update("")
                case sg.WIN_CLOSED:
                    break
                case "Exit":
                    break
        delete_window.close()
    except IndexError:
        pass