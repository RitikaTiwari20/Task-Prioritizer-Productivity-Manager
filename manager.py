from operator import attrgetter
from task import Task

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, title, deadline, priority):
        self.tasks.append(Task(title, deadline, priority))

    def view_tasks(self):
        sorted_tasks = sorted(
            [task for task in self.tasks if not task.completed],
            key=lambda t: (t.days_left(), t.priority)
        )
        return sorted_tasks

    def complete_task(self, title):
        for task in self.tasks:
            if task.title.lower() == title.lower() and not task.completed:
                task.completed = True
                return True
        return False

    def delete_task(self, title):
        for i, task in enumerate(self.tasks):
            if task.title.lower() == title.lower():
                del self.tasks[i]
                return True
        return False

    def search_tasks(self, keyword):
        return [task for task in self.tasks if keyword.lower() in task.title.lower()]
