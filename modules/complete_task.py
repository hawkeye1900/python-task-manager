from modules import (get_completed_tasks,
                     get_outstanding_todos,
                     get_task_summary)


def complete_task(window, values):
    all_completed_tasks = get_completed_tasks("r")
    all_tasks = get_outstanding_todos("r")
    completed_task = values["listOfTasks"][0]

    for index, task in enumerate(all_tasks):
        if task.split(";")[0] == completed_task:
            all_tasks.remove((all_tasks[index]))
            all_completed_tasks.append(task)
            break

    get_outstanding_todos("w", all_tasks)
    get_completed_tasks("w", all_completed_tasks)

    window["listOfTasks"].update(values=get_task_summary(
        all_tasks))