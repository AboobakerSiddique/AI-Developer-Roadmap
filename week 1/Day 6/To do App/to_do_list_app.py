import os

folder = os.path.dirname(__file__)
file_path = os.path.join(folder, "tasks.txt")

tasks = []


def load_tasks():
    """Load tasks from tasks.txt into the global `tasks` list."""
    global tasks
    tasks = []

    if not os.path.exists(file_path):
        return

    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue

            # Format: task|status
            parts = line.split("|", 1)
            if len(parts) != 2:
                continue

            task_text = parts[0]
            status = parts[1]
            tasks.append({"task": task_text, "status": status})


def save_tasks():
    """Save the current `tasks` list into tasks.txt."""
    with open(file_path, "w", encoding="utf-8") as f:
        for t in tasks:
            f.write(f"{t['task']}|{t['status']}\n")


def normalize_task_name(name: str) -> str:
    return " ".join(name.strip().split()).lower()


def get_counts():
    total = len(tasks)
    pending = sum(1 for t in tasks if t.get("status") == "Pending")
    completed = sum(1 for t in tasks if t.get("status") == "Completed")
    return total, pending, completed


def render_tasks_list(task_list, heading: str = "TO-DO LIST"):
    if len(task_list) == 0:
        print("\nNo tasks available.\n")
        return

    print(f"\n-------- {heading} --------")
    for index, task in enumerate(task_list, start=1):
        print(f"{index}. {task['task']} - {task['status']}")
    print("----------------------------")


def view_tasks():
    render_tasks_list(tasks, heading="TO-DO LIST")


def add_task():
    new_task = input("Enter the task: ").strip()
    if new_task == "":
        print("Task cannot be empty.")
        return

    new_norm = normalize_task_name(new_task)

    # Prevent duplicates by name (case-insensitive)
    for t in tasks:
        if normalize_task_name(t["task"]) == new_norm:
            print("Task already exists. Duplicate tasks are not allowed.")
            return

    task = {
        "task": new_task.capitalize(),
        "status": "Pending",
    }

    tasks.append(task)
    save_tasks()
    print("Task added successfully!")


def mark_complete():
    if len(tasks) == 0:
        print("\nNo tasks available.\n")
        return

    render_tasks_list(tasks, heading="TO-DO LIST")

    try:
        task_num = int(input("\nEnter the task number to mark as completed: "))
        if 1 <= task_num <= len(tasks):
            tasks[task_num - 1]["status"] = "Completed"
            save_tasks()
            print("Task marked as completed!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter numbers only.")


def delete_task():
    if len(tasks) == 0:
        print("\nNo tasks available.\n")
        return

    render_tasks_list(tasks, heading="TO-DO LIST")

    try:
        task_num = int(input("\nEnter the task number to delete: "))
        if 1 <= task_num <= len(tasks):
            removed = tasks.pop(task_num - 1)
            save_tasks()
            print(f"Deleted task: {removed['task']}")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter numbers only.")


def edit_task():
    if len(tasks) == 0:
        print("\nNo tasks available.\n")
        return

    render_tasks_list(tasks, heading="TO-DO LIST")

    try:
        task_num = int(input("\nEnter the task number to edit (rename): "))
        if not (1 <= task_num <= len(tasks)):
            print("Invalid task number.")
            return

        current = tasks[task_num - 1]["task"]
        new_name = input(f"Enter new name for '{current}': ").strip()

        if new_name == "":
            print("Task name cannot be empty.")
            return

        new_norm = normalize_task_name(new_name)

        # Prevent duplicates (excluding the task being edited)
        for i, t in enumerate(tasks):
            if i == task_num - 1:
                continue
            if normalize_task_name(t["task"]) == new_norm:
                print("Another task with the same name already exists. Rename cancelled.")
                return

        tasks[task_num - 1]["task"] = new_name.capitalize()
        save_tasks()
        print("Task renamed successfully!")
    except ValueError:
        print("Please enter numbers only.")


def search_tasks():
    keyword = input("Enter keyword to search: ").strip()
    if keyword == "":
        print("Keyword cannot be empty.")
        return

    keyword_norm = keyword.lower()
    matches = [t for t in tasks if keyword_norm in t["task"].lower()]
    render_tasks_list(matches, heading=f"SEARCH RESULTS for '{keyword}'")


def pending_completed_summary():
    total, pending, completed = get_counts()
    print("\nTask Summary")
    print(f"Total: {total}")
    print(f"Pending: {pending}")
    print(f"Completed: {completed}\n")


def sort_and_view_tasks():
    if len(tasks) == 0:
        print("\nNo tasks available.\n")
        return

    # Pending first, then Completed
    tasks_sorted = sorted(tasks, key=lambda t: 0 if t.get("status") == "Pending" else 1)
    tasks.clear()
    tasks.extend(tasks_sorted)


    save_tasks()
    render_tasks_list(tasks, heading="TO-DO LIST (Pending first)")


def exit_app():
    # Extra safety: persist latest state on exit
    save_tasks()
    print("\nThank you for using the To-Do List App!")
    print("Goodbye! 👋")


load_tasks()

while True:
    print("\nTo-Do List App")
    print("----------------")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Mark a task as completed")
    print("4. Delete a task")
    print("5. Edit a task (rename)")
    print("6. Search tasks")
    print("7. Pending vs Completed counts")
    print("8. Sort tasks (Pending first)")
    print("9. Exit")
    print("----------------")

    choice = input("Enter your choice (1-9): ")

    try:
        choice_num = int(choice)
        if choice_num == 1:
            add_task()
        elif choice_num == 2:
            view_tasks()
        elif choice_num == 3:
            mark_complete()
        elif choice_num == 4:
            delete_task()
        elif choice_num == 5:
            edit_task()
        elif choice_num == 6:
            search_tasks()
        elif choice_num == 7:
            pending_completed_summary()
        elif choice_num == 8:
            sort_and_view_tasks()
        elif choice_num == 9:
            exit_app()
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 9.")
    except ValueError:
        print("Please enter numbers only.")

