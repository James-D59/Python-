import os


os.system("cls")

'''
 our list will be in this format
 tasks = [{"task": "Task 1", "completed": False},
          {"task": "Task 2", "completed": True},
          {"task": "Task 3", "completed": False}]
 ]

'''

# Add a task to the list
def add_task(tasks, task):
    # Append the task to the list
    tasks.append({"task": task, "completed": False})
    print(f'Task "{task}" has been added.')
    return tasks


# View all tasks in the list
def view_tasks(tasks):
    if not tasks:
        print("No tasks in the list.")
    else:
        print("\n--- To-Do List ---")
        for idx, task_info in enumerate(tasks, start=1):
            status = "Done" if task_info["completed"] else "Not Done"
            print(f"{idx}. {task_info['task']} - {status}")
    print()


            

# Remove a task from the list
def remove_task(tasks, task_index):
    if 0 <= task_index < len(tasks):
        removed_task = tasks.pop(task_index)
        print(f'Task "{removed_task["task"]}" has been removed.')
    else:
        print("Invalid task number.")
    return tasks

# Mark task as complete
def mark_task_complete(tasks, task_index):
    if 0 <= task_index < len(tasks):
        tasks[task_index]["completed"] = True
        print(f'Task "{tasks[task_index]["task"]}" has been marked as complete.')
    else:
        print("Invalid task number.")
    return tasks

# Main to do function
def to_do_list_app():
    # Create a python list to keep track of our to do list
    tasks = []

    while True:
        os.system("cls")
        print("\n--- To-Do List Menu  ----")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Remove Task")
        print("4. Mark Task as Complete")
        print("5. Exit")

        choice = input("Choose an Option (1-5): ")

        if choice == '1':
            task = input("Enter the task: ")
            tasks = add_task(tasks, task)
            #tell the user to hit enter
            input("Press Enter to Continue...") #puase before clearing the screen
        elif choice == '2':
            view_tasks(tasks)
            input("Press Enter to Continue...")
        
        elif choice == '3':
            if tasks:
                view_tasks(tasks) #show the list before prompting the user to remove one
                task_index = int(input("Enter the task number to remove: ")) - 1
                # call the remove task function and pass intm to remove he list
                tasks = remove_task(tasks, task_index)
            else:
                print("There are no tasks to remove...")
            input("Press Enter to Continue...")
            
        elif choice == '4':
            if tasks:
                view_tasks(tasks) #show the list before prompting the user to mark one complete
                task_index = int(input("Enter the task number to mark as complete: ")) - 1
                tasks = mark_task_complete(tasks, task_index)
            else:
                print("There are no tasks to mark as complete...")

            input("Press Enter to Continue...")
        
        elif choice == '5':
            print("Exiting the To-Do List. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")
            input("Press Enter to Continue...")

# Run the to do list application
to_do_list_app()


