import pymongo
import time
from functools import wraps  
# Your connection
connectionString = "mongodb+srv://manojsaini653733_db_user:7mUuKvsYRBkRICcF@cluster0.noljb9f.mongodb.net/?retryWrites=true&w=majority"
client = pymongo.MongoClient(connectionString)
db = client['projects']
todos = db['todoList']

class TodoList:
    def __init__(self):
        self.todos=db['todoList']

    def decForTime(delay=0):  
        def decorator(func):  
            @wraps(func)
            def calcTimeofExec(*args, **kwargs):  
                start=time.perf_counter()
                if(delay>0):
                    time.sleep(delay)
                result = func(*args, **kwargs)  
                end=time.perf_counter()
                print(f"Time taken for execution of {func.__name__} {end-start}")
                return result  
            return calcTimeofExec
        return decorator
  

    # COMPLETE CRUD FUNCTIONS - SAME USE CASES AS PLAIN CODE
    @decForTime(2)
    def add_task(self,task_name):
        """Add new task to todoTask array"""
        self.todos.update_one({}, {'$push': {'todoTask': task_name}}, upsert=True)
        print(f"✅ Added: '{task_name}'")

    @decForTime(1)
    def list_tasks(self):
        """Show all tasks with numbers"""
        tasks = self.get_all_tasks()
        if not tasks:
            print("📭 No tasks!")
            return
        print("\n📋 Your Tasks:")
        for i, task in enumerate(tasks):
            print(f"  {i+1}. {task}")


    def get_all_tasks(self):
        """Get raw task list"""
        doc = self.todos.find_one({}, {'todoTask': 1})
        return doc['todoTask'] if doc and 'todoTask' in doc else []

    @decForTime()
    def update_task():
        """Update task by number"""
        tasks = TodoList.get_all_tasks()
        if not tasks:
            print("📭 No tasks to update!")
            return
        
        TodoList.list_tasks()
        try:
            index = int(input("Enter task number to update: ")) - 1
            if 0 <= index < len(tasks):
                new_task = input("Enter new task name: ")
                todos.update_one({}, {'$set': {f'todoTask.{index}': new_task}})
                print("✅ Task updated!")
            else:
                print("❌ Invalid number!")
        except:
            print("❌ Invalid input!")

    @decForTime()
    def delete_task():
        """Delete task by number"""
        tasks = TodoList.get_all_tasks()
        if not tasks:
            print("📭 No tasks to delete!")
            return
        
        TodoList.list_tasks()
        try:
            index = int(input("Enter task number to delete: ")) - 1
            if 0 <= index < len(tasks):
                task_name = tasks[index]
                todos.update_one({}, {'$pull': {'todoTask': task_name}})
                print("✅ Task deleted!")
            else:
                print("❌ Invalid number!")
        except:
            print("❌ Invalid input!")

    @decForTime()
    def clear_all():
        """Delete all tasks"""
        todos.update_one({}, {'$set': {'todoTask': []}})
        print("All tasks cleared!")    

        

# MAIN MENU (same as your plain code)

def main_menu():
    todoList1=TodoList()
    while True:
        print("\n🚀 TODO APP (MongoDB)")
        print("1. Add task")
        print("2. List tasks")
        print("3. Update task")
        print("4. Delete task")
        print("5. Clear all")
        print("0. Exit")
        
        choice = input("Choose option: ")
        
        if choice == '1':
            task = input("Enter task: ")
            todoList1.add_task(task)
        elif choice == '2':
            todoList1.list_tasks()
        elif choice == '3':
            todoList1.update_task()
        elif choice == '4':
            todoList1.delete_task()
        elif choice == '5':
            todoList1.clear_all()
        elif choice == '0':
            print("Goodbye!")
            break
        else:
            print("❌ Invalid option!")

if __name__ == '__main__':
    main_menu()
    client.close()
