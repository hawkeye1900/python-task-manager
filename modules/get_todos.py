filepath = "files/todos.txt"


def get_todos(mode, data=None, file_arg=filepath):
    with open(file_arg, mode) as local_file:
        if mode == "r":
            tasks = local_file.readlines()
            print(tasks)
            return tasks
        elif mode == "w":
            local_file.writelines(data)
            return None


def get_task_summary(list):
    task_summaries = []
    for task in list:
        task_summaries.append(task.split(";")[0])
    return task_summaries


if __name__ == "__main__":
    print(f"__name__ = {__name__}: Directly running function")
