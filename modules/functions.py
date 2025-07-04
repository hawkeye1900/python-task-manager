import FreeSimpleGUI as sg

filepath = "files/todos.txt"


def get_todos(mode, data=None, file_arg=filepath):
    with open(file_arg, mode) as local_file:
        if mode == "r":
            tasks = local_file.readlines()
            return tasks
        elif mode == "w":
            local_file.writelines(data)
            return None


def edit_task():
    try:
        all_tasks = get_todos("r")
        layout = [
            [sg.Text("Task for editing", size=(15, 1)),
             sg.InputText(key="editTask")],
            [sg.Listbox(values=all_tasks,
                        key="listOfTasks",
                        size=(45, 8),
                        text_color="white",
                        enable_events=True)],
            [sg.Save(), sg.Cancel()]
        ]

        edit_window = sg.Window("Edit Window",
                               layout,
                               font=("Helvetica", 20))

        while True:
            event, values = edit_window.read()

            match event:
                case "listOfTasks":
                    if values["listOfTasks"]:
                        print(values)
                        (edit_window["editTask"]
                         .update(value=values["listOfTasks"][0]
                                 .strip("\n")))

                case "Save":
                    # edit_window.close()
                    # task_to_edit = values["listOfTasks"][0]
                    # print(task_to_edit)

                    # edit_window["Selected task"].update(taskToEdit)
                    #
                    # # Enter new task
                    # editedTask = values["Selected task"]
                    # print(editedTask)
                    #
                    # # Get tasklist from .txt
                    # # tasksList = functions.get_todos("r")
                    # print(tasksList)
                    #
                    # # Update tasklist list
                    # index = tasksList.index(taskToEdit)
                    # tasksList[index] = editedTask + "\n"
                    # functions.get_todos("w", tasksList)
                    # edit_window["Selected task"].update("")
                    # edit_window["listOfTasks"].update(values=tasksList)
                    break
                case "Cancel":
                    break
                case sg.WIN_CLOSED:
                    break

        edit_window.close()
    except IndexError:
        pass




if __name__ == "__main__":
    print(f"__name__ = {__name__}: Directly running function")
