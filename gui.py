import sys
from modules import functions
import FreeSimpleGUI as fsg


print(sys.executable)

taskInputLabel = fsg.Text("Enter task:")
taskInputField = fsg.InputText(tooltip="Enter new task")
deleteBtn = fsg.Button("Delete")
submitBtn = fsg.Button("Submit")
exitBtn = fsg.Button("Exit")


layout = [
    [taskInputLabel, taskInputField, deleteBtn],
    [submitBtn, exitBtn]
]


# Create an instance of window type
window = fsg.Window("Task Manager", layout)

# the read() method displays the window instance on the screen
window.read()
window.close()
