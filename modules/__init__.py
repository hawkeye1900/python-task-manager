# modules/__init__.py

from .get_todos import (get_outstanding_todos,
                        get_task_summary,
                        get_completed_tasks,
                        get_all_tasks)
from .add_task import add_task
from .edit_task import edit_task
from .complete_task import complete_task
from .delete_task import delete_task
from .detailed_add import detailed_add
from .views import view_current_tasks, view_completed_tasks

