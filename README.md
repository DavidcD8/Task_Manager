
# Task Manager

A simple Python-based console application to manage tasks. The application allows users to add, edit, view, delete, and mark tasks as completed.

## Features

- **Add Tasks**: Add tasks with a name and description.
- **Edit Tasks**: Modify the name and description of existing tasks.
- **View Tasks**: Display all tasks with their details.
- **Delete Tasks**: Mark tasks as completed.
- **Delete Tasks**: Remove tasks from the task list.
- **Mark as Completed** (Feature placeholder for future updates).

## Getting Started

### Prerequisites
- Python 3.x installed on your machine.
- SQLite (SQLite comes bundled with Python by default).
## How to Use
1. Follow the on-screen menu to perform actions:
   - Press `1` to add a task.
   - Press `2` to edit a task.
   - Press `3` to view all tasks.
   - Press `4` to mark as completed.
   - Press `5` to delete a task.
2. Enter the required information when prompted.
3. The program will display updates or results for your actions.

## Example
```1: Add task
2: Edit task
3: View all Tasks
4: Mark as completed
5: Remove task
Choose an option: 1
Enter task name: Call Mom
Enter task description: Call Mom tonight to check in
Task added successfully!


=== Task List ===
1:
  Name       : test 1
  Description: test 1
  Completed  : No
----------------------------------------
```

## Error Handling and Fixes

### 1. **Issue: Task ID skipping**
   - **Error**: When adding new tasks, the ID skips numbers (e.g., after adding tasks with IDs 1, 2, 4, 5). This happens due to the way SQLite's `AUTOINCREMENT` works; it doesn't reuse IDs from deleted tasks.
   - **Fix**: This behavior is expected with `AUTOINCREMENT`. If necessary, you can reset the ID sequence after deleting tasks by running the following SQL command:
     ```
     DELETE FROM sqlite_sequence WHERE name = 'tasks';
     ```

### 2. **Issue: Invalid task ID input**
   - **Error**: If a user enters an invalid task ID (e.g., a non-numeric value or a task ID that doesn't exist), the program would allow processing, potentially leading to unexpected behavior.

   - **Fix**: I implemented validation to ensure that only numeric values are accepted as valid task IDs. Additionally, we check that the task ID exists before proceeding with updates or deletions. If an invalid ID is provided, an error message is displayed, and the process is halted.
   - **Example fix in the code**:
     ```python
     if not task_id.isdigit():  # Check if input is a valid number
         print("Invalid task ID.")
         return
     task_id = int(task_id)
     ```

### 3. **Issue: Task not appearing in order**
   - **Error**: Tasks added may not appear in the order they were added due to the `AUTOINCREMENT` behavior in SQLite.
   - **Fix**: The application does not explicitly control the task ID order. However, you can modify the code to fetch tasks in the desired order using SQL's `ORDER BY` clause. For example, adding `ORDER BY id` to the `SELECT` query will ensure tasks are displayed in the order of their IDs:
     ```python
     cur.execute("SELECT id, name, description, completed FROM tasks ORDER BY id")
     ```

### 4. **Issue: Task completion status not updating**
   - **Error**: The application might not update the task's completion status if an invalid or non-existent task ID is entered.
   - **Fix**: The code was modified to properly validate the task ID before attempting to mark it as completed. A message will now indicate if the task ID does not exist.

### 5. **Issue: Input validation for menu options**
   - **Error**: If the user enters a non-numeric value or an invalid number outside the valid range (1-5) when selecting an option from the menu, the program would not handle it properly.
   - **Fix**: I added a validation step to ensure the input is numeric and within the allowed range (1-5). This prevents invalid choices from being processed.
   - **Example fix in the code**:
     ```python
     if not user_input.isdigit() or int(user_input) not in range(1, 6):
         print("Invalid option. Please choose a number between 1 and 5.")
     ```

### 6. **Issue: Tasks not being deleted from the database**
   - **Error**: Sometimes tasks weren't being deleted properly from the database.
   - **Fix**: The `DELETE` query was adjusted to ensure the task ID is correctly validated before deleting. If an invalid task ID is entered, a message will be displayed, and no action will be taken.

