to_do_list = []

def add_task(task):
    to_do_list.append(task)
    print(f"The '{task}' added.")

def view_tasks():
    if to_do_list:
        print("Your tasks:")
        for i, task in enumerate(to_do_list, 1):
            print(f"{i}. {task}")
    else:
        print(" Invalid task number.")

def remove_task(task_number):
    if 0 < task_number <= len(to_do_list):
        remove = to_do_list.pop(task_number - 1)
        print(f"Task '{remove}' remove.")
    else:
        print("Invalid task number.")

while True:
    print("\n1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == "1":
        task = input("Enter the task: ")
        add_task(task)
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        view_tasks()
        task_number = int(input("Enter the task number to remove: "))
        remove_task(task_number)
    elif choice == "4":
        break
    else:
        print("Invalid choice. Please try again.")