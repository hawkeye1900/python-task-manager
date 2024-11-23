filepath = "files/todos.txt"


def get_todos(mode, data=None, file_arg=filepath):
    with open(file_arg, mode) as local_file:
        if mode == "r":
            tasks = local_file.readlines()
            return tasks
        elif mode == "w":
            local_file.writelines(data)
            return None


def show(arr):
    print("\n")
    if len(arr) > 0:
        print("No. Task")
        for i, item in enumerate(arr):
            print(f"{i + 1}: {item.capitalize().strip("\n")}")
        print("\n")
    else:
        print("Currently no tasks to show\n")


# Every Python module (file) has a special built-in variable called __name__.
# When a Python file is executed directly, the value of __name__ is set to "__main__".
# This can be used to control what parts of a file run when file is called as a module
# or when it is called directly
if __name__ == "__main__":
    # if functions module is run directly, its __name__ variable is set to __main__
    print(f"__name__ = {__name__}: Directly running function")
# else:
#     print(f"__name__ = {__name__}: function running as a module")
