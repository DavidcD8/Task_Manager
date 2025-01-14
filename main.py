import sqlite3

# Initialize database
con = sqlite3.connect("task_manager.db")
cur = con.cursor()

# Create table if it doesn't exist
cur.execute("""
CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    description TEXT NOT NULL,
    completed BOOLEAN DEFAULT 0
)
""")

con.commit()

def print_menu():  # Prints menu
    print("1: Add task")
    print("2: Edit task")
    print("3: View all Tasks")
    print("4: Mark as completed")
    print("5: Remove task\n")

    user_input = input("Choose an option: ")

    if not user_input.isdigit() or int(user_input) not in range(1, 6):  # Check if input is a valid number between 1 and 5
        print("Invalid option. Please choose a number between 1 and 5.")
    else:
        process_choice(int(user_input))  # Pass directly to the processing function


def process_choice(user_input): # process the user input and calls the appropiate function
    if user_input == 1:
        print("\n📌 Adding a new task. Please provide the details.\n")
        add_task()
    elif user_input == 2:
        print("\n✏️ Editing an existing task. Let's update it.\n")
        edit_task()
    elif user_input == 3:
        print("\n📋 Displaying all tasks:\n")
        view_tasks()
    elif user_input == 4:
        print("\n✅ Marking a task as completed. Select a task from the list.\n")
        mark_as_completed()
    elif user_input == 5:
        print("\n🗑️ Deleting a task. Choose the task to remove.\n")
        delete_task()


def add_task():  # Adds task to database
    print("Enter task name: ")
    name = input()
    print("Enter task description: ")
    description = input()
    cur.execute("INSERT INTO tasks (name, description) VALUES (?, ?)", (name, description)) # Insert task into the database without specifying ID
    con.commit()
    print("Task added successfully!")


def edit_task():  # Edit task in database
    view_tasks()
    task_id = input("Enter the task ID to edit: ").strip()
    if not task_id.isdigit():  # Check if input is a valid number
        print("Invalid task ID.")
        return
    task_id = int(task_id)

    name = input("Enter new task name: ").strip()
    description = input("Enter new task description: ").strip()
    if name and description:
        cur.execute("UPDATE tasks SET name = ?, description = ? WHERE id = ?", (name, description, task_id))
        con.commit()
        print("Task updated successfully!")
    else:
        print("Task name and description cannot be empty!")


def view_tasks():  # prints all the tasks
    cur.execute("SELECT id, name, description, completed FROM tasks")
    tasks = cur.fetchall()  # Returns all the tasks from the database
    if not tasks:
        print("No tasks available!")
        return
    print("\n=== Task List ===")
    for task in tasks:
        completed = "Yes" if task[3] else "No"  # checks if it's completed or not
        print(f"{task[0]}:")
        print(f"  Name       : {task[1]}")
        print(f"  Description: {task[2]}")
        print(f"  Completed  : {completed}")
        print("-" * 40 + "\n")  # Separator for readability


def mark_as_completed():  # Mark a task as completed
    view_tasks()  # Display all tasks
    task_id = input("Enter the task ID to mark as completed: ").strip()

    if not task_id.isdigit():  # Check if input is a valid number
        print("Invalid task ID. Please enter a valid number.")
        return

    task_id = int(task_id)
    cur.execute("SELECT id FROM tasks WHERE id = ?", (task_id,)) # Check if the task ID exists in the database
    task = cur.fetchone()

    if task is None:  # If no task is found with the provided ID
        print(f"No task found with ID {task_id}. Please enter a valid task ID.")
        return


    cur.execute("UPDATE tasks SET completed = 1 WHERE id = ?", (task_id,))
    con.commit()
    print("Task marked as completed!")


def delete_task():  # Delete task from database
    view_tasks()
    task_id = input("Enter the task ID to delete: ").strip()
    if not task_id.isdigit():
        print("Invalid task ID.")
        return
    task_id = int(task_id)

    cur.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
    con.commit()
    print("Task deleted successfully!")


def main():
    while True:
        print_menu()


if __name__ == '__main__':
    main()
