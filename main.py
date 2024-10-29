todos = []


def show():
    if len(todos) == 0:
        print("No tasks to show")
    else:
        print("No. Task")
        for i, item in enumerate(todos):
            print(f"{i + 1}: {item.capitalize()}")
    print("\n")


while True:
    choice = input("Enter what you want to do from the following options:"
                   "\nadd"
                   "\nshow"
                   "\nedit"
                   "\ncomplete"
                   "\nexit\n: ")
    choice = choice.strip().lower()
    match choice:
        case "add":
            todo = input("Enter a task: ")
            todos.append(todo)
        case "show":
            show()
        case 'edit':
            if len(todos) == 0:
                print("No tasks to edit")

            while True:
                print("From the following list of tasks, enter the number of the task to edit")
                show()
                try:
                    selected = int(input("Choice: ")) - 1
                    if selected < 0 or selected >= len(todos):
                        raise IndexError("You must select the number of a task from the list shown.")
                except (ValueError, IndexError) as e:
                    if isinstance(e, ValueError):
                        print("\033[91mINVALID INPUT\033[0m: Please enter a valid number.")
                    elif isinstance(e, IndexError):
                        print("\033[91mINVALID INPUT\033[0m: You must select the number of a task from the list shown.")
                    continue
                new_task = input("Enter your new task: ")
                todos[selected] = new_task
                print("New task updated successfully")
                show()
                break
        case "complete":
            print("From the following list of tasks, enter the number of the task to complete")
            show()
            number = int(input("Choice: ")) - 1
            todos.pop(number)
            show()
        case "exit":
            break
        case _:
            print("You entered an unknown command")
print("Bye!")

