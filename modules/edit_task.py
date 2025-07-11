import FreeSimpleGUI as sg
from modules import (get_outstanding_todos, get_task_summary)
from datetime import datetime


def edit_task(window):
    try:
        all_tasks = get_outstanding_todos("r")
        layout = [
            [sg.Text("Summary",
                     size=(12, 1),
                     pad=(0, 5),
                     font=14,
                     text_color="#000000",
                     background_color="#fad787"),
             sg.InputText(key="summary",
                          pad=(10, 5),
                          font=14,
                          background_color="#fad787",
                          text_color="#000000")],
            [sg.Text("Description",
                     size=(12, 1),
                     pad=(0, 5),
                     font=14,
                     text_color="#000000",
                     background_color="#fad787"),
             sg.InputText(key="description",
                          pad=(10, 5),
                          font=14,
                          text_color="#000000",
                          background_color="#fad787")],
            [sg.Text("Priority",
                     size=(12, 1),
                     pad=(0, 5),
                     font=14,
                     text_color="#000000",
                     background_color="#fad787"),
             sg.InputText("Current Priority",
                          key="priority",
                          size=(20, 1),
                          pad=(10, 5),
                          font=14,
                          text_color="#000000",
                          background_color="#fad787"),
             sg.Combo(["Low", "Medium", "High"],
                      default_value="Low",
                      pad=(3, 5),
                      key="set_priority",
                      font=14,
                      text_color="#000000",
                      background_color="#fad787",
                      enable_events=True,)
             ],
            [sg.CalendarButton("Due Date",
                               key="calendar",
                               pad=(0, 5),
                               font=12),
             sg.InputText("Current Saved Date: ",
                          key="date",
                          visible=True,
                          size=(24, 1),
                          pad=(10, 5),
                          font=14,
                          text_color="#000000",
                          background_color="#fad787",
                          enable_events=True)],
            [sg.Listbox(values=get_task_summary(all_tasks),
                        key="listOfTasks",
                        size=(45, 8),
                        text_color="#000000",
                        enable_events=True,
                        font=14,
                        tooltip="Select a task to edit",
                        background_color="#fad787")],
            [sg.Save(bind_return_key=True, pad=(0, 5), font=12),
             sg.Cancel(pad=(3, 5), font=12),
             sg.Exit(pad=(3, 5), font=12),
             sg.Text("Error: Semi-colon ; is an invalid character",
                     visible=False,
                     key="error",
                     background_color="red",
                     text_color="yellow",
                     pad=(10, 0),
                     font=14)
             ]
        ]

        edit_window = sg.Window("Edit Window",
                                layout,
                                font=("Helvetica", 20),
                                background_color="#fad787")

        formatted_date = ""
        while True:
            edit_window.refresh()
            event, values = edit_window.read()

            match event:
                case "listOfTasks":
                    # Update edit fields with details of selected task
                    if values["listOfTasks"]:
                        selected_task = values["listOfTasks"][0].strip("\n")
                        for index, task in enumerate(all_tasks):
                            if selected_task == task.split(";")[0]:
                                (edit_window["summary"]
                                 .update(task.split(";")[0]))
                                (edit_window["description"]
                                 .update(task.split(";")[1]))
                                (edit_window["date"]
                                 .update(task.split(";")[2]))
                                (edit_window["priority"]
                                 .update(task.split(";")[3]))
                    continue
                case "date":
                    due_date = values["date"]
                    parsed_date = datetime.strptime(due_date,
                                                    "%Y-%m-%d %H:%M:%S")
                    formatted_date = parsed_date.strftime("%A, %B %d, %Y")
                    (edit_window["date"].update(formatted_date))
                    continue
                case "set_priority":
                    priority = values["set_priority"]
                    edit_window["priority"].update(priority)
                    continue
                case "Save":
                    task_being_edited = values["listOfTasks"][0].strip("\n")
                    for index, task in enumerate(all_tasks):
                        if task.split(";")[0] == task_being_edited:
                            date = values["date"]
                            if not date:
                                date = datetime.now()
                                formatted_date = date.strftime("%A, %B %d, %Y")
                            if "\n" in {values["summary"]}:
                                sg.popup("You entered an invalid character - \\n")
                                break
                            edited_task = (f"{values["summary"].strip('\n')};"
                                           f"{values["description"].strip('\n')};"
                                           f"{formatted_date};"
                                           f"{values["priority"].strip('\n')}")

                            all_tasks[index] = edited_task + "\n"
                            get_outstanding_todos("w", all_tasks)

                            # Resetting inputs
                            edit_window["summary"].update("")
                            edit_window["description"].update("")
                            edit_window["date"].update("")
                            edit_window["priority"].update("Low")
                            edit_window["listOfTasks"].update(
                                values=get_task_summary(all_tasks))
                            window["listOfTasks"].update(
                                values=get_task_summary(all_tasks))
                            continue
                case "Cancel":
                    edit_window["summary"].update("")
                    edit_window["description"].update("")
                    edit_window["date"].update("")
                    edit_window["priority"].update("Low")
                    edit_window["listOfTasks"].update(
                        values=get_task_summary(all_tasks))
                    window["listOfTasks"].update(
                        values=get_task_summary(all_tasks))
                    continue
                case sg.WIN_CLOSED:
                    break
                case "Exit":
                    break

        edit_window.close()
    except IndexError:
        pass