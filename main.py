
def check_todos():
    with open("files/todos.txt", "r") as file:
        tasks = file.readlines()

    if len(tasks) == 0:
        print("Currently no tasks to show\n")
        return None
    else:
        return tasks


def show(arr):
    print("\n")
    if arr:
        print("No. Task")
        for i, item in enumerate(arr):
            print(f"{i + 1}: {item.capitalize().strip("\n")}")
    else:
        print("Currently no tasks to show\n")


todos = check_todos()
print(todos)
while True:
    choice = input("Enter what you want to do from the following options: "
                   "\nadd"
                   "\nshow"
                   "\nedit"
                   "\ncomplete"
                   "\nexit\n: ")
    choice = choice.strip().lower()

    # menu options below
    match choice:
        case "add":
            todo = input("Enter a task: ") + "\n"

            with open("files/todos.txt", "r") as file:
                todos = file.readlines()

            todos.append(todo)

            with open("files/todos.txt", "w") as file:
                file.writelines(todos)

        case "show":
            show(todos)
        case 'edit':
            if not todos:
                print("No tasks to edit\n")
                continue
            while True:
                try:
                    show(todos)
                    selected = int(input("Enter the number of the task to edit: ")) - 1
                    if selected < 0 or selected >= len(todos):
                        raise IndexError("You must select the number of a task from the list shown.")
                except (ValueError, IndexError) as e:
                    if isinstance(e, ValueError):
                        print("\033[91mINVALID INPUT\033[0m: Please enter a valid number.")
                    elif isinstance(e, IndexError):
                        print("\033[91mINVALID INPUT\033[0m: You must select the number of a task from the list shown.")
                    continue
                new_task = input("Enter your new task: ")
                todos[selected] = f"{new_task}\n"
                print("New task updated successfully")
                show(todos)
                with open("files/todos.txt", "w") as file:
                    file.writelines(todos)
                break
        case "complete":
            print("From the following list of tasks, enter the number of the task to complete")
            show(todos)
            number = int(input("Choice: ")) - 1
            todos.pop(number)
            with open("files/todos.txt", "w") as file:
                file.writelines(todos)
            show(todos)
        case "exit":
            break
        case _:
            print("You entered an unknown command")
print("Bye!")

