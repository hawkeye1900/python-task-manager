import FreeSimpleGUI as sg
from datetime import datetime
from modules import (get_todos, get_task_summary)


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
            [sg.Text("Summary",
                     size=(12, 1), pad=(0, 5)),
             sg.InputText(key="summary", pad=(3, 5))],
            [sg.Text("Description",
                     size=(12, 1), pad=(0, 5)),
             sg.InputText(key="description", pad=(3, 5))],
            [sg.CalendarButton("Due Date",
                               key="calendar", pad=(0, 5))],
            [sg.Text("Priority",
                     size=(12, 1),
                     pad=(0, 5)),
             sg.Combo(["Low", "Medium", "High"],
                      pad=(3, 5),
                      key="priority")],
            [sg.Save(bind_return_key=True, pad=(0, 5)),
             sg.Cancel(pad=(3, 5)),
             sg.Exit(pad=(3, 5)),
             sg.Text("Error: Semi-colon ; is an invalid character",
                     visible=False,
                     key="error",
                     background_color="red",
                     text_color="yellow",
                     pad=(10, 0))
             ]
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
                    (window["listOfTasks"]
                    .update(values=get_task_summary(
                        all_tasks)))

                    reset_inputs(detailed_add_window)
                    continue
                case "Cancel":
                    reset_inputs(detailed_add_window)
                    continue

        detailed_add_window.close()
    except:
        pass
