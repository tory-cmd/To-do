#create to do stuff
#welcome user, ask what to add, show tasks in bar, give it a completed, and a not completed Task, and be able to remove
def menu():
    print("Welcome to the todo list!")
    print("1. Add a task")
    print("2. Remove a task")
    print("3. Show all tasks")
    print("4. Show complete tasks")
    print("5. Mark as done")
    print("6. Exit")
    int(input("Please select an option: "))
tasks = []
def taskAdd(): #option 1


    taskInput = input("Enter a task to add: ")
    tasks.append({"task": taskInput, "done": False})


    print(f"Awesome! you have added {taskInput}")


def removeTask():
    if not tasks:
        print("No tasks to remove!")
        return


    for index, task in enumerate(tasks, start=1):
        print(f"{index}. {task}")

    choiceRemove = int(input("Please choose the number of the task to remove: "))

    if choiceRemove == 1:
        tasks.pop(choiceRemove)
    # figure out removal logic

def showTasks():
    print("All tasks:")
    print(tasks)


def showCompleteTasks():
    print("All complete tasks:")


def markDone():
    for index, task in enumerate(tasks, start=1):
        print(f"{index}. {task}")

    input("What task would you like to mark done?:")





def exitList():



menu()
taskAdd()
markDone()