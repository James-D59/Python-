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
def view_tasks():
    pass

# Remove a task from the list
def remove_task():
    pass

# Mark task as complete
def mark_task_complete():
    pass

# Main todo function
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
            view_tasks()
        elif choice == '3':
            remove_task()
        elif choice == '4':
            mark_task_complete()
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

# Run the to do list application
to_do_list_app()


