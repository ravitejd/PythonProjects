import os
import json
from datetime import datetime

file_path = 'tasks.json'

# Check if the tasks.json file exists, if not create it
if not os.path.isfile(file_path):
    with open(file_path, 'w') as f:
        json.dump([], f)
    print(f"{file_path} created.")
else:
    print(f"{file_path} already exists.")

# Choose the fuction to perfom an action
# Add, Update, Remove, List
arg = input("What would you like to do among Add, Update, Remove, List : ").strip()

def add():
    task = input("Enter the task to add: ")
    # Create a new task dictionary
    dict = {
        "ID": len(json.load(open(file_path))) + 1,
        "TASK_NAME": task,
        "TASK_STATUS": "Pending",
        "LastUpdatedDate": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    # Read existing tasks, append the new task, and write back to the file
    with open(file_path, 'r') as f:
        tasks = json.load(f)
        tasks.append(dict)
    with open(file_path, 'w') as f:
        json.dump(tasks, f, indent=4)

    list()
    return

def update():
    task_id = int(input("Enter the ID of the task to update: "))
    updated_task_name = input("Enter the new task name or enter to update status: ")
    updated_status = input("Enter the new status (Pending/Inprogress/Completed): ")

    with open(file_path, 'r') as f:
        tasks =json.load(f)
        for task in tasks:
            if task['ID'] == task_id:
                if updated_task_name:
                    task['TASK_NAME'] = updated_task_name
                if updated_status in ["Pending", "Completed", "Inprogress"] or updated_status in ["pending", "completed", "inprogress"]:
                    task['TASK_STATUS'] = updated_status
                task['LastUpdatedDate'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                break
    with open(file_path, 'w') as f:
        json.dump(tasks, f, indent=4)

    print(f"Task {updated_task_name} updated and the status is {updated_status}.")
    return

def remove():
    task_id = int(input("Enter the ID of the task to remove: "))
    with open(file_path, 'r') as f:
        tasks = json.load(f)
        for task in tasks:
            if task['ID'] == task_id:
                tasks.remove(task)
                break
    with open(file_path, 'w') as f:
        json.dump(tasks, f, indent=4)
    print(f"Task with ID {task_id} removed.")
    return

def list():
    with open(file_path, 'r') as f:
        tasks = json.load(f)
    if not tasks:
        print("No tasks available.")
    else:
        print ("ID\tTASK_NAME\tTASK_STATUS\tLastUpdatedDate")
        for task in tasks:
            print(f"{task['ID']}\t{task['TASK_NAME']}\t{task['TASK_STATUS']}\t{task['LastUpdatedDate']}")
    return


if arg == 'add' or arg == 'Add':
    add()

elif arg == 'update' or arg == 'Update':
    update()

elif arg == 'remove' or arg == 'Remove':
    remove()

elif arg == 'List' or arg == 'list':
    list()



