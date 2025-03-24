import os

task = []
def show_tasks():
    if not tasks:
        print("No tasks available.")
    else: 
        print("Your Tasks:")
        for idx, task in enumerate(tasks, 1):
            status = "Completed" if task['completed'] else "Pending"
            print(f"{idx}. {task['task_name']} - {status}")  

