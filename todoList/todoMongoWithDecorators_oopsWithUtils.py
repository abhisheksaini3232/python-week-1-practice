from utils import client, db, todos, TodoList

def main_menu():
    todoList1=TodoList()
    while True:
        print("\n TODO APP ")
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
            print("Invalid option!")

if __name__ == '__main__':
    main_menu()
    client.close()
