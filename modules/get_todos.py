filepath = "files/todos.txt"
filepath_completed_tasks = "files/completed.txt"


def get_outstanding_todos(mode, data=None, file_arg=filepath):
    with open(file_arg, mode) as local_file:
        if mode == "r":
            tasks = local_file.readlines()
            return tasks
        elif mode == "w":
            local_file.writelines(data)
            return None


def get_task_summary(tasks):
    task_summaries = []
    for task in tasks:
        task_summaries.append(task.split(";")[0])
    return task_summaries


def get_completed_tasks(mode, data=None, file_arg=filepath_completed_tasks):
    with open(file_arg, mode) as local_file:
        if mode == "r":
            tasks = local_file.readlines()
            return tasks
        elif mode == "w":
            local_file.writelines(data)
            return None


def get_all_tasks():
    outstanding = get_outstanding_todos("r")
    completed = get_completed_tasks("r")
    all_tasks = outstanding + completed
    return all_tasks


if __name__ == "__main__":
    print(f"__name__ = {__name__}: Directly running function")
