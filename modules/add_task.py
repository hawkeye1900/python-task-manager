import FreeSimpleGUI as sg
from datetime import datetime
from .get_todos import get_todos


def add_task(values, window):
    new_task = values["New task"]
    if not new_task:
        print("Invalid")
        return
    if "\n" in new_task:
        sg.popup("You entered an invalid character - \\n")
        values["New task"] = ""

    task = new_task + "\n"
    tasks_list = get_todos("r")
    tasks_list.append(task)
    get_todos("w", tasks_list)

    window["New task"].update("")
    window["listOfTasks"].update(values=tasks_list)


def reset_inputs(inputs):
    defaults = {
        "summary": "",
        "description": "",
        "priority": "",
    }

    for key in defaults:
        inputs[key].update(defaults[key])

    inputs["error"].update(visible=False)


def detailed_add(window):
    try:
        layout = [
            [sg.Text("Summary", size=(12, 1)), sg.InputText(
                key="summary")],
            [sg.Text("Description", size=(12, 1)), sg.InputText(
                key="description")],
            [sg.CalendarButton("Due Date", key="calendar")],
            [sg.Text("Priority", size=(12, 1)),
             sg.Combo(["Low", "Medium", "High"], key="priority")],
            [sg.Exit(),
             sg.Save(bind_return_key=True),
             sg.Cancel(),
             sg.Text("Error: Semi-colon ; is an invalid character",
                     visible=False,
                     key="error")]
        ]

        detailed_add_window = sg.Window("Detailed Add Window",
                                        layout,
                                        font=("Helvetica", 20),
                                        background_color="#800000")
        while True:
            event, values = detailed_add_window.read()

            match event:
                case "Exit":
                    break
                case "Save":
                    if any(";" in value for value in values.values()):
                        detailed_add_window["error"].update(visible=True)
                        continue

                    due_date = values["calendar"]
                    if not due_date:
                        due_date = datetime.now()
                        formatted_date = due_date.strftime("%A, %B %d, %Y")
                    else:
                        parsed_date = datetime.strptime(due_date,
                                                        "%Y-%m-%d %H:%M:%S")
                        formatted_date = parsed_date.strftime("%A, %B %d, %Y")

                    task = (f'{values["summary"]};'
                            f'{values["description"]};'
                            f'{values["priority"]};'
                            f'{formatted_date})')
                    print(task)
                    all_tasks = get_todos("r")
                    task = task + "\n"
                    all_tasks.append(task)
                    get_todos("w", all_tasks)
                    window["listOfTasks"].update(values=all_tasks)

                    reset_inputs(detailed_add_window)
                    continue
                case "Cancel":
                    reset_inputs(detailed_add_window)
                    continue

        detailed_add_window.close()
    except:
        pass




