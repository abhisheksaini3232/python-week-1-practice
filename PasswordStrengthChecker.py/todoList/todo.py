todoList=[]
def add():
  x=input("Enter the task you want to add in the list: ")
  todoList.append(x)
  print(todoList)

def delete():
  x=input("Enter the task you want to delete from the list: ")
  todoList.delete(x)
  print(todoList)



  
option=int(input("Enter the options to add or delete(1->add,\n2->delete,\n3->List completed:"): ")
a=0
while(a=0): 
  if(option==1):
        add()
  elif(option==1):
        delete()  
  else:
      print("The value entered was not appropriate") 



      
  
    



      


