task_list = []
task_id_counter = 1


def display_menu():
    print("\n===== STUDENT TASK MANAGEMENT SYSTEM =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Completed")
    print("4. Delete Task")
    print("5. Exit")


def add_task():
    global task_id_counter
    title = input("Enter task title: ")
    task = {
        "id": task_id_counter,
        "title": title,
        "status": "Pending"
    }
    task_list.append(task)
    task_id_counter += 1
    print("Task added successfully!")


def view_tasks():
    if not task_list:
        print("No tasks available.")
        return

    print("\n--- TASK LIST ---")
    for task in task_list:
        print(f"ID: {task['id']} | Title: {task['title']} | Status: {task['status']}")


def complete_task():
    task_id = int(input("Enter task ID to mark as completed: "))
    for task in task_list:
        if task["id"] == task_id:
            task["status"] = "Completed"
            print("Task marked as completed!")
            return
    print("Task not found.")


def delete_task():
    task_id = int(input("Enter task ID to delete: "))
    for task in task_list:
        if task["id"] == task_id:
            task_list.remove(task)
            print("Task deleted successfully!")
            return
    print("Task not found.")


def main():
    while True:
        display_menu()
        choice = input("Select option: ")

        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            complete_task()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            print("Exiting system...")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
