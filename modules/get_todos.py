filepath = "files/todos.txt"


def get_todos(mode, data=None, file_arg=filepath):
    with open(file_arg, mode) as local_file:
        if mode == "r":
            tasks = local_file.readlines()
            return tasks
        elif mode == "w":
            local_file.writelines(data)
            return None


if __name__ == "__main__":
    print(f"__name__ = {__name__}: Directly running function")
