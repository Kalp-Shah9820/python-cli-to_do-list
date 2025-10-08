import json
import os

# File to store the tasks
FILE_NAME = "tasks.json"

# Function to load tasks from the JSON file
def load_tasks():
    if not os.path.exists(FILE_NAME):
        return []
    with open(FILE_NAME, "r") as file:
        return json.load(file)

# Function to save tasks to the JSON file
def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file, indent=4)

# Function to display all tasks
def view_tasks(tasks):
    if not tasks:
        print("\nNo tasks found.")
        return
    print("\nYour Tasks:")
    for i, task in enumerate(tasks, start=1):
        status = "✔️" if task["completed"] else "❌" 
        print(f"{i}. {task['title']} [{status}]")

# Function to add a new task
def add_task(tasks):
    title = input("\nEnter the task title: ").strip()
    if not title:
        print("Task title cannot be empty!")
        return
    tasks.append({"title": title, "completed": False})
    save_tasks(tasks)
    print("Task added successfully!")

# Function to update an existing task
def update_task(tasks):
    view_tasks(tasks)
    try:
        task_num = int(input("\nEnter the task number to update: "))
        if 1 <= task_num <= len(tasks):
            new_title = input("Enter the new title: ").strip()
            if not new_title:
                print("Task title cannot be empty!")
                return
            tasks[task_num - 1]["title"] = new_title
            save_tasks(tasks)
            print("Task updated successfully!")
        else:
            print("Invalid task number!")
    except ValueError:
        print("Please enter a valid number!")

# Function to delete a task
def delete_task(tasks):
    view_tasks(tasks)
    try:
        task_num = int(input("\nEnter the task number to delete: "))
        if 1 <= task_num <= len(tasks):
            deleted_task = tasks.pop(task_num - 1)
            save_tasks(tasks)
            print(f"Task '{deleted_task['title']}' deleted successfully!")
        else:
            print("Invalid task number!")
    except ValueError:
        print("Please enter a valid number!")

# Function to mark a task as completed
def mark_task_completed(tasks):
    view_tasks(tasks)
    try:
        task_num = int(input("\nEnter the task number to mark as completed: "))
        if 1 <= task_num <= len(tasks):
            tasks[task_num - 1]["completed"] = True
            save_tasks(tasks)
            print(f"Task '{tasks[task_num - 1]['title']}' marked as completed!")
        else:
            print("Invalid task number!")
    except ValueError:
        print("Please enter a valid number!")

# Main function to display the menu and handle user input
def main():
    tasks = load_tasks()
    
    while True:
        print("\nTo-Do List Application")
        print("-----------------------")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Mark Task as Completed")
        print("6. Exit")
        
        choice = input("\nEnter your choice (1-6): ").strip()
        
        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            update_task(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            mark_task_completed(tasks)
        elif choice == "6":
            print("Exiting the application. Goodbye!")
            break
        else:
            print("Invalid choice! Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()
