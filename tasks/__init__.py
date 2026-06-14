"""Task implementations"""

from .task1 import Task1
from .task2 import Task2
from .task3 import Task3

TASK_MAP = {
    "task1": Task1,
    "task2": Task2,
    "task3": Task3,
}

__all__ = ["Task1", "Task2", "Task3", "TASK_MAP"]
