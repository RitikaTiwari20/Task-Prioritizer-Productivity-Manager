from manager import TaskManager

manager = TaskManager()

def menu():
    print("\n=== Task Prioritizer & Productivity Manager ===")
    print("1. Add Task")
    print("2. View All Tasks")
    print("3. Complete Task")
    print("4. Delete Task")
    print("5. Search Task")
    print("6. Exit")

while True:
    menu()
    choice = input("Enter choice: ")

    if choice == '1':
        title = input("Task Title: ")
        deadline = input("Deadline (YYYY-MM-DD): ")
        print("Priority: 1 (High), 2 (Medium), 3 (Low)")
        priority = int(input("Enter Priority: "))
        manager.add_task(title, deadline, priority)
        print("Task added!")

    elif choice == '2':
        tasks = manager.view_tasks()
        if not tasks:
            print("No pending tasks.")
        else:
            print("\n--- Upcoming Tasks ---")
            for task in tasks:
                print(task)

    elif choice == '3':
        title = input("Enter task title to mark as complete: ")
        if manager.complete_task(title):
            print("Marked as complete.")
        else:
            print("Task not found.")

    elif choice == '4':
        title = input("Enter task title to delete: ")
        if manager.delete_task(title):
            print("Task deleted.")
        else:
            print("Task not found.")

    elif choice == '5':
        keyword = input("Enter keyword to search: ")
        results = manager.search_tasks(keyword)
        if results:
            for task in results:
                print(task)
        else:
            print("No matching tasks found.")

    elif choice == '6':
        print("Goodbye! Stay productive. 🚀")
        break

    else:
        print("Invalid choice.")
