import pymongo
import time
from pymongo import MongoClient
from functools import wraps
from pymongo.errors import PyMongoError, ConnectionFailure, ServerSelectionTimeoutError

# MongoDB connection
connectionString = "mongodb://localhost:27017/"
client = pymongo.MongoClient(connectionString)
db = client['projects']
todos = db['todoList']

def mongo_connection_check(client):
 def decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            # client = args[0].client  # self.client
            client.admin.command('ping')
            print("MongoDB connection OK")
        except (ConnectionFailure, ServerSelectionTimeoutError, PyMongoError) as e:
            print(f"MongoDB connection failed: {str(e)}")
            return None
        return func(*args, **kwargs)
    return wrapper
 return decorator

class TodoList:
    def __init__(self, connection_string="mongodb://localhost:27017/"):
        self.client = MongoClient(connection_string)
        self.todos = self.client.todo_db.todos


    def decForTime(delay=0):
        def decorator(func):
            @wraps(func)
            def calcTimeofExec(*args, **kwargs):
                start = time.perf_counter()
                if delay > 0:
                    time.sleep(delay)
                result = func(*args, **kwargs)
                end = time.perf_counter()
                print(f"Time taken for {func.__name__}: {end-start:.4f}s")
                return result
            return calcTimeofExec
        return decorator

    @mongo_connection_check(client)
    @decForTime(0)
    def add_task(self, task_name):
        self.todos.update_one({}, {'$push': {'todoTask': task_name}}, upsert=True)
        print(f"Added: '{task_name}'")

    @mongo_connection_check(client)
    @decForTime(1)
    def list_tasks(self):
        tasks = self.get_all_tasks()
        if not tasks:
            print("No tasks!")
            return
        print("\nYour Tasks:")
        for i, task in enumerate(tasks):
            print(f"  {i+1}. {task}")

    def get_all_tasks(self):
        doc = self.todos.find_one({}, {'todoTask': 1})
        return doc['todoTask'] if doc and 'todoTask' in doc else []

    @mongo_connection_check(client)
    @decForTime(0)
    def update_task(self):
        tasks = self.get_all_tasks()
        if not tasks:
            print("No tasks to update!")
            return
        
        self.list_tasks()
        try:
            index = int(input("Enter task number to update: ")) - 1
            if 0 <= index < len(tasks):
                new_task = input("Enter new task name: ")
                self.todos.update_one({}, {'$set': {f'todoTask.{index}': new_task}})
                print("Task updated!")
            else:
                print("Invalid number!")
        except ValueError:
            print("Invalid input! Enter numbers only.")

    @mongo_connection_check(client)
    @decForTime(0)
    def delete_task(self):
        tasks = self.get_all_tasks()
        if not tasks:
            print("No tasks to delete!")
            return
        
        self.list_tasks()
        try:
            index = int(input("Enter task number to delete: ")) - 1
            if 0 <= index < len(tasks):
                task_name = tasks[index]
                self.todos.update_one({}, {'$pull': {'todoTask': task_name}})
                print("Task deleted!")
            else:
                print("Invalid number!")
        except ValueError:
            print("Invalid input!")

    @mongo_connection_check(client)
    @decForTime(0)
    def clear_all(self):
        self.todos.update_one({}, {'$set': {'todoTask': []}})
        print("All tasks cleared!")

