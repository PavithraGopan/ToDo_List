import json

class Task:
    def __init__(self, title, description, category):
        self.title = title
        self.description = description
        self.category = category
        self.completed = False

    def mark_completed(self):
        self.completed = True

    def __repr__(self):
        return f"Task(title={self.title}, description={self.description}, category={self.category}, completed={self.completed})"

def save_tasks(tasks):
    with open('tasks.json', 'w') as f:
        json.dump([task.__dict__ for task in tasks], f)

def load_tasks():
    try:
        with open('tasks.json', 'r') as f:
            return [Task(**data) for data in json.load(f)]
    except FileNotFoundError:
        return []

def display_tasks(tasks):
    if not tasks:
        print("No tasks available.")
        return
    for i, task in enumerate(tasks):
        status = "Completed" if task.completed else "Pending"
        print(f"{i + 1}. {task.title} [{task.category}] - {status}\n   {task.description}")

def add_task(tasks):
    title = input("Enter the task title: ")
    description = input("Enter the task description: ")
    category = input("Enter the task category (e.g., Work, Personal, Urgent): ")
    task = Task(title, description, category)
    tasks.append(task)
    print(f"Task '{title}' added successfully.")

def mark_task_completed(tasks):
    if not tasks:
        print("No tasks available to mark as completed.")
        return
    display_tasks(tasks)
    task_num = int(input("Enter the task number to mark as completed: "))
    if 1 <= task_num <= len(tasks):
        tasks[task_num - 1].mark_completed()
        print(f"Task '{tasks[task_num - 1].title}' marked as completed.")
    else:
        print("Invalid task number.")

def delete_task(tasks):
    if not tasks:
        print("No tasks available to delete.")
        return
    display_tasks(tasks)
    task_num = int(input("Enter the task number to delete: "))
    if 1 <= task_num <= len(tasks):
        task = tasks.pop(task_num - 1)
        print(f"Task '{task.title}' deleted successfully.")
    else:
        print("Invalid task number.")

def main():
    tasks = load_tasks()
    while True:
        print("\n--- Personal To-Do List ---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task Completed")
        print("4. Delete Task")
        print("5. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            display_tasks(tasks)
        elif choice == '3':
            mark_task_completed(tasks)
        elif choice == '4':
            delete_task(tasks)
        elif choice == '5':
            save_tasks(tasks)
            print("Tasks saved. Exiting the application.")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == '__main__':
    main()
