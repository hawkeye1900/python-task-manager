import FreeSimpleGUI as sg
from datetime import datetime
from modules import get_outstanding_todos, get_task_summary


def reset_inputs(inputs):
    defaults = {
        "summary": "",
        "description": "",
        "priority": "Low",
        "calendar_display": ""
    }

    for key in defaults:
        inputs[key].update(defaults[key])

    inputs["error"].update(visible=False)


def detailed_add(window):
    try:
        layout = [
            [sg.Text("Summary",
                     size=(12, 1), pad=(0, 5), font=14),
             sg.InputText(key="summary",
                          pad=(3, 5),
                          font=14,
                          background_color="#800000")],
            [sg.Text("Description",
                     size=(12, 1), pad=(0, 5), font=14),
             sg.InputText(key="description",
                          pad=(3, 5),
                          font=14,
                          background_color="#800000")],
            [sg.Text("Priority",
                     size=(12, 1),
                     pad=(0, 5), font=14),
             sg.Combo(["Low", "Medium", "High"],
                      default_value="Low",
                      pad=(3, 5),
                      key="priority",
                      font=14,
                      background_color="#800000")],
            [sg.CalendarButton("Due Date",
                               key="calendar",
                               pad=(0, 5),
                               font=12),
             sg.InputText(key="calendar_display",
                          pad=(3, 5),
                          font=14,
                          background_color="#800000",
                          enable_events=True)
             ],

            [sg.Save(bind_return_key=True, pad=(0, 5), font=12),
             sg.Cancel(pad=(3, 5), font=12),
             sg.Exit(pad=(3, 5), font=12),
             sg.Text("Error: Semi-colon ; is an invalid character",
                     visible=False,
                     key="error",
                     text_color="yellow",
                     background_color="#800000",
                     pad=(10, 0),
                     font=14)
             ]
        ]

        detailed_add_window = sg.Window("Detailed Add Window",
                                        layout,
                                        font=("Helvetica", 20),
                                        background_color="#800000",
                                        finalize=True)
        formatted_date = ""
        due_date = ""
        while True:
            event, values = detailed_add_window.read()

            match event:
                case sg.WIN_CLOSED:
                    break
                case "Exit":
                    break
                case "calendar_display":
                    due_date = values["calendar_display"]
                    parsed_date = datetime.strptime(due_date,
                                                    "%Y-%m-%d %H:%M:%S")
                    formatted_date = parsed_date.strftime("%A, %B %d, %Y")
                    (detailed_add_window["calendar_display"]
                     .update(formatted_date))
                    continue
                case "Save":
                    if any(";" in value for value in values.values()):
                        detailed_add_window["error"].update(visible=True)
                        continue
                    if not due_date:
                        due_date = datetime.now()
                        formatted_date = due_date.strftime("%A, %B %d, %Y")
                    task = (
                        f'{values["summary"]};'
                        f'{values["description"]};'
                        f'{formatted_date};'
                        f'{values["priority"]};'
                    )
                    all_tasks = get_outstanding_todos("r")
                    all_tasks.append(task + "\n")
                    get_outstanding_todos("w", all_tasks)

                    window["listOfTasks"].update(values=get_task_summary(
                        all_tasks))

                    reset_inputs(detailed_add_window)
                    due_date = ""
                    continue
                case "Cancel":
                    reset_inputs(detailed_add_window)
                    continue

        detailed_add_window.close()
    except:
        pass
