from datetime import datetime

class Task:
    def __init__(self, title, deadline, priority):
        self.title = title
        self.deadline = datetime.strptime(deadline, "%Y-%m-%d")
        self.priority = priority  # 1 (High), 2 (Medium), 3 (Low)
        self.completed = False

    def days_left(self):
        return (self.deadline - datetime.today()).days

    def __str__(self):
        status = "✓" if self.completed else "⏳"
        return f"[{status}] {self.title} | Due: {self.deadline.date()} | Priority: {self.priority} | Days Left: {self.days_left()}"
