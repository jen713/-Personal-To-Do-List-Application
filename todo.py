import json

class Task:
    def __init__(self, title, description, category):
        self.title = title
        self.description = description
        self.category = category
        self.completed = False

    def mark_completed(self):
        self.completed = True

def save_tasks(tasks, file_name='tasks.json'):
    with open(file_name, 'w') as f:
        json.dump([task.__dict__ for task in tasks], f, indent=4)

def load_tasks(file_name='tasks.json'):
    try:
        with open(file_name, 'r') as f:
            return [Task(**data) for data in json.load(f)]
    except FileNotFoundError:
        return []

def add_task(tasks):
    title = input("Enter the title of the task: ")
    description = input("Enter the description of the task: ")
    category = input("Enter the category of the task (e.g., Work, Personal, Urgent): ")
    tasks.append(Task(title, description, category))
    save_tasks(tasks)
    print("Task added successfully!")

def view_tasks(tasks):
    if not tasks:
        print("No tasks available.")
        return
    for idx, task in enumerate(tasks, start=1):
        status = "Completed" if task.completed else "Not completed"
        print(f"{idx}. Title: {task.title}, Description: {task.description}, Category: {task.category}, Status: {status}")

def mark_task_completed(tasks):
    view_tasks(tasks)
    if tasks:
        task_num = int(input("Enter the number of the task to mark as completed: ")) - 1
        if 0 <= task_num < len(tasks):
            tasks[task_num].mark_completed()
            save_tasks(tasks)
            print("Task marked as completed!")
        else:
            print("Invalid task number.")

def delete_task(tasks):
    view_tasks(tasks)
    if tasks:
        task_num = int(input("Enter the number of the task to delete: ")) - 1
        if 0 <= task_num < len(tasks):
            tasks.pop(task_num)
            save_tasks(tasks)
            print("Task deleted successfully!")
        else:
            print("Invalid task number.")

def main():
    tasks = load_tasks()

    while True:
        print("\nTo-Do List Menu:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task Completed")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Choose an option (1, 2, 3, 4, 5): ")

        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            view_tasks(tasks)
        elif choice == '3':
            mark_task_completed(tasks)
        elif choice == '4':
            delete_task(tasks)
        elif choice == '5':
            save_tasks(tasks)
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()
