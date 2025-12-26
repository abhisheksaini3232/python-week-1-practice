todoList=[]
def add():
  x=input("Enter the task you want to add in the list: ")
  todoList.append(x)
  print(todoList)

def delete():
  x=input("Enter the task you want to delete from the list: ")
  todoList.delete(x)
  print(todoList)


while true:
  option=int(input("Enter the options to add or delete(1->add,2->delete): "))  
  if(option==1):
    add()
  elif(option==1):
    delete()  
  else:
    print("Enter from the given options")
    continue




    


