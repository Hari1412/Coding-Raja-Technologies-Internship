import json
import os
from datetime import datetime

# Function to load tasks from a file
def load_tasks(filename):
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            return json.load(file)
    else:
        return []

# Function to save tasks to a file
def save_tasks(tasks, filename):
    with open(filename, 'w') as file:
        json.dump(tasks, file)

# Function to add a task
def add_task(tasks):
    task_name = input("Enter task name: ")
    priority = input("Enter priority (high, medium, low): ")
    due_date = input("Enter due date (YYYY-MM-DD): ")
    tasks.append({"name": task_name, "priority": priority, "due_date": due_date, "completed": False})

# Function to remove a task
def remove_task(tasks):
    print_tasks(tasks)
    index = int(input("Enter the index of the task to remove: "))
    if 0 <= index < len(tasks):
        del tasks[index]
    else:
        print("Invalid index")

# Function to mark a task as completed
def mark_completed(tasks):
    print_tasks(tasks)
    index = int(input("Enter the index of the task to mark as completed: "))
    if 0 <= index < len(tasks):
        tasks[index]["completed"] = True
    else:
        print("Invalid index")

# Function to display tasks
def print_tasks(tasks):
    for i, task in enumerate(tasks):
        print(f"{i}. [{task['priority']}] {task['name']} - Due: {task['due_date']} - {'Completed' if task['completed'] else 'Pending'}")

# Main function
def main():
    filename = "tasks.json"
    tasks = load_tasks(filename)

    while True:
        print("\n===== TO-DO LIST =====")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. Mark Task as Completed")
        print("4. View Tasks")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            remove_task(tasks)
        elif choice == "3":
            mark_completed(tasks)
        elif choice == "4":
            print_tasks(tasks)
        elif choice == "5":
            save_tasks(tasks, filename)
            print("Exiting...")
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
