my_tasks={}
task_id=1
def AddTasks(task_count):
    global tasks
    global task_id
    for i in range(task_count):
        task=input("Enter the task:")
        my_tasks[task_id]={"tasks":task,"status":False}
        task_id+=1

def UpdateTasks(tid):
    global my_tasks
    task = my_tasks.get(tid)
    try:
        task['status'] = not task['status']
        print("Task updated successfully")
    except Exception as e:
        print(e)
        print("Failed to update task")


def DeleteTasks(project):
    try:
        tasks.pop(project)
        print("Task deleted successfully")
        ShowTasks()
    except Exception as e:
        print(e)
        print("Failed delete task")

def ShowTasks():
    global my_tasks
    if not my_tasks:
         print("No tasks found.")
    return
    print("Task:")
    for t in my_tasks:
        status="Done" if my_tasks[t]['status'] else "incomplete"
        print(f"[{t}]{tasks[t]['tasks']}-['status']")

while True:
   print("ToDo Project")
   print("1.Add Tasks:\n2.Update Tasks:\n3.Delete Tasks:\n4.Show Tasks:")
   try:
      choice=int(input("Enter your choice:"))
   except ValueError:
       print(("Invalid input.Enter a number"))
       continue
   if choice == 1:
       try:
           task_count = int(input("How many tasks do you wish to add? "))
           AddTasks(task_count)
       except ValueError:
           print("Please enter a valid number.")
   elif choice == 2:
       try:
           tid = int(input("Enter task ID to update: "))
           UpdateTasks(tid)
       except ValueError:
           print("Invalid task ID.")
   elif choice == 3:
       try:
           ShowTasks()
           tid = int(input("Enter task ID to delete: "))
           DeleteTasks(tid)
       except ValueError:
           print("Invalid task ID.")
   elif choice == 4:
       ShowTasks()
   elif choice == 5:
       print("Exiting ToDo Project.")
       break
   else:
       print("Invalid choice. Please again.")






# id=1
# my_tasks={}
# def AddTask(n):
#     global my_tasks
#     global id
#     for t in range(n):
#         task=input("Enter the task : ")
#         my_tasks[id]={"tasks":task,"status":False}
#         id+=1
# def ShowTasks():
#     for todo in my_tasks:
#         print(f"{todo} {my_tasks[todo]["tasks"]} - {"Done" if my_tasks[todo]["status"]else "Incomplete"}")
#
# def Update(task_id):
#     task=my_tasks.get(task_id,"Tasks not found")
#     task['status']=not task['status']
#     ShowTasks()
# def DeleteTask(task_id):
#     try:
#         my_tasks.pop(task_id)
#     except KeyError:
#         print("Tasks not found")
#     except Exception:
#         print("Error")
# while True:
#     print("ToDo Project")
#     print("1.Add Task\n2.Update Task\n3.Show Tasks\n4.Delete Tasks")
#     choice=int(input("Enter your choice : "))
#     if choice==1:
#         task_count=int(input("How many tasks do you wish to add : "))
#         AddTask(task_count)
#     elif choice==2:
#         task_id=int(input("Enter the task id to be updated : "))
#         Update(task_id)
#     elif choice==3:
#         ShowTasks()
#     elif choice==4:
#         task_id = int(input("Enter the task id to be deleted : "))
#         DeleteTask(task_id)


       
