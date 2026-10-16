#to-do
tasks = []
def menu():
    print("Welcome to the todo list!")
    print("1. Add a task")
    print("2. Remove a task")
    print("3. Show all tasks")
    print("4. Mark as done")
    print("5. Exit")

def taskAdd(): #option 1


    taskInput = input("Enter a task to add: ")
    tasks.append({"task": taskInput, "done": False})


    print(f"Awesome! you have added {taskInput}")

def removeTask():
    showTasks()
    if not tasks:
        print("No tasks to remove!")
        return

    try:
        index = int(input("Please choose the number of the task to remove: ")) - 1
        if 0 <= index < len(tasks):
            removed = tasks.pop(index)
            print(f"we removed {removed['task']}")
        else:
            print("Invalid task!")
    except ValueError:
            print("Please put a valid number!")


    # figure out removal logic

def showTasks():
    print("All tasks:")
    for index, task in enumerate(tasks, start=1):
        status = "Y" if task["done"] else "N"
        print(f"{index}. {task['task']} [{status}]")

def markDone():
    showTasks()
    if not tasks:
        return
    try:
        index = int(input("What task would you like to mark done?:")) - 1
        if 0 <= index < len(tasks):
            tasks[index]["done"] = True
            print("Done!")

        else:
            print("Invalid task!")
    except ValueError:
        print("Please put a valid number!")

while True:
    menu()
    choice = int(input("Please select an option: "))

    if choice == 1:
        taskAdd()
    elif choice == 2:
        removeTask()
    elif choice == 3:
        showTasks()
    elif choice == 4:
        markDone()
    elif choice == 5:
        print("Thank you for using this program!")
        break
    else:
        print("Invalid option!")
