from modules import (get_completed_tasks,
                     get_outstanding_todos,
                     get_task_summary)


def complete_task(window, values):
    all_completed_tasks = get_completed_tasks("r")
    all_tasks = get_outstanding_todos("r")
    print(all_completed_tasks)
    completed_task = values["listOfTasks"][0]
    print(completed_task)

    for index, task in enumerate(all_tasks):
        if task.split(";")[0] == task:
            index_of_task = index
            all_tasks.remove((all_tasks[index_of_task]))
            all_completed_tasks.append(completed_task)
            break

    get_outstanding_todos("w", all_tasks)
    get_completed_tasks("w", all_completed_tasks)

    window["listOfTasks"].update(values=get_task_summary(
        all_tasks))
    window["New task"].update("")