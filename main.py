def print_menu(tasks):
    print("1: Add task")
    print("2: Edit task")
    print("3: View all Tasks")
    print("4: Mark as completed")
    print("5: Remove task")
    
    try:
        user_input = int(input("Choose an option: "))  # Convert input to an integer
        if user_input not in range(1, 6):  # Validate option
            raise ValueError("Invalid option. Please choose a number between 1 and 5.")
    except ValueError as e:
        print(e)
    else:
        process_choice(user_input, tasks)  # Call your processing function


def process_choice(user_input, tasks):
    if int(user_input) == 1:
        print("\n📌 Adding a new task. Please provide the details.")
        add_task(tasks)
    elif int(user_input) == 2:
        print("\n✏️ Editing an existing task. Let's update it.")
        edit_task(tasks)
    elif int(user_input) == 3:
        print("\n📋 Displaying all tasks:")
        view_tasks(tasks)
    elif int(user_input) == 4:
        print("\n✅ Marking a task as completed. Select a task from the list.")
        mark_as_completed(tasks)
    elif int(user_input) == 5:
        print("\n🗑️ Deleting a task. Choose the task to remove.")
        delete_task(tasks)



def add_task(tasks):
    view_tasks(tasks)
    print("Enter a name: ")
    name = input()
    print("Enter Description: ")
    description = input()
    task = {"name": name, "description": description, "completed": False}   # Add the task to the list of tasks
    tasks.append(task)
    print("Task added successfully!")  # Feedback


def edit_task(tasks): # Access the task dictionary directly and update the 'name' and 'description' field
    if not tasks:
        print("There are no tasks!")
    try:
        view_tasks(tasks)
        task_to_edit = input("Choose a task to edit by number: ") # Get the task number as input
        if not task_to_edit.isdigit() or int(task_to_edit) < 1 or int(task_to_edit) > len(tasks):
            raise ValueError("Invalid task number. Please enter a valid number.")
        
        new_task_name = input("Enter a new name: ")  # Get the new name as input
        if not new_task_name:  # Ensure the task name is not empty.
            raise ValueError("Task name cannot be blank.")
         
        current_task = tasks[int(task_to_edit) - 1]  # Convert to zero-based index
        current_task["name"] = new_task_name  # Update the task name
        print("Task name updated successfully!")  # Feedback
        
        
        new_description = input("Enter a new description: ").strip()  # Prompt the user for a new task description and validate input.
        if not new_description:  # Ensure the description is not empty.
            raise ValueError("Task description cannot be blank.")
 
        current_task["description"] = new_description  # Update the task description
        print("Task description updated successfully!")  # Feedback

    except ValueError as e:
        # Handle invalid input errors and display appropriate feedback to the user.
        print(e)
        
def view_tasks(tasks):
    if not tasks:
        print("No tasks available! ")
        return
    for index, task in enumerate(tasks, start=1):
        print(f"Task {index}:")
        print(f"  Name: {task['name']}")
        print(f"  Description: {task['description']}")
        print(f"  Completed: {task['completed']}\n")


def mark_as_completed(tasks):
    if not tasks:
        print("No tasks available to mark as completed!")
        return
    else:
        view_tasks(tasks)  # Display all tasks
        print("Choose a task to mark as completed: ")
        task_index = input()  # Get the task number
        try:
            tasks[int(task_index) - 1]["completed"] = True  # Update the 'completed' status to True
            print(f"Task {task_index} marked as completed successfully!")
        except (IndexError, ValueError):
            print("Invalid task number. Please try again.")




def delete_task(tasks):
    if not tasks:  # Checks if there are tasks available
        print("No tasks available! ")
        return
    else:
        view_tasks(tasks)  # Displays all tasks
        print("Select Task to delete")  # Prompts user
        task_to_delete = input()  # Get the task number as input
        del tasks[int(task_to_delete) - 1]  # Deletes task from list using del
        print("Task deleted successfully!")  # Feedback


def main():
    tasks = []  # Use a list to store multiple tasks
    while True:
        print_menu(tasks)


if __name__ == '__main__':
    main()
