from modules import functions
import time


now = time.strftime("%H:%M on %b %d, %Y ")
print(f"It is {now}")

while True:
    choice = input("Choose one of the following options: "
                   "\nadd <enter task>"
                   "\nshow"
                   "\nedit"
                   "\ncomplete"
                   "\nexit\n: ")

    choice = choice.strip().lower()

    if choice.startswith("add"):
        todo = f"{choice[4:]}" + '\n'

        todos = functions.get_todos("r")
        todos.append(todo)
        functions.get_todos("w", todos)

    elif choice.startswith("show"):
        todos = functions.get_todos("r")
        functions.show(todos)
    elif choice.startswith("edit"):
        todos = functions.get_todos("r", data=None)
        functions.show(todos)
        if not todos:
            continue
        while True:
            try:
                selected = int(input("Enter the number of the task to edit: ")) - 1
                if selected < 0 or selected >= len(todos):
                    raise IndexError("\033[91mINVALID INPUT\033[0m: You must select the "
                                     "number of a task from the list shown.")
            except (ValueError, IndexError) as e:
                if isinstance(e, ValueError):
                    print("\033[91mINVALID INPUT\033[0m: Please enter a valid number.")
                elif isinstance(e, IndexError):
                    print("\033[91mINVALID INPUT\033[0m: You must select the number of a task from the list shown.")
                continue
            new_task = input("Enter your new task: ")
            todos[selected] = f"{new_task}\n"
            print("New task updated successfully")
            functions.show(todos)
            with open("files/todos.txt", "w") as file:
                file.writelines(todos)
            break
    elif choice.startswith("complete"):
        print("From the following list of tasks, enter the number of the task to complete")
        functions.show(todos)
        number = int(input("Choice: ")) - 1
        todos.pop(number)
        with open("files/todos.txt", "w") as file:
            file.writelines(todos)
        functions.show(todos)
    elif choice.startswith("exit"):
        break
    else:
        print("You entered an unknown command\nEnter a valid command\n")
print("Bye!")

