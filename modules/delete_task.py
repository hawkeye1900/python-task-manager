from .get_todos import get_completed_tasks
import FreeSimpleGUI as sg


def delete_task(window):
    try:
        completed = get_completed_tasks("r")
        layout = [
            [sg.InputText(key="delete_task", font=14)],
            [sg.Button("Delete task?", key="Delete", font=12)],
            [sg.Listbox(values=completed,
                        key="listOfTasks",
                        size=(45, 8),
                        text_color="white",
                        enable_events=True,
                        font=14)],
            [sg.Exit(font=12), sg.Cancel(font=12)]
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
                        index_of_task = completed.index(task_to_be_deleted)
                        completed.remove(completed[index_of_task])

                        get_completed_tasks("w", completed)
                        delete_window["delete_task"].update("")
                        delete_window["listOfTasks"].update(values=completed)
                        window["listOfTasks"].update(values=completed)
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