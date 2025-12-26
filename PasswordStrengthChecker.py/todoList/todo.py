todoList=[]
def add():
  x=input("Enter the task you want to add in the list: ")
  todoList.append(x)
  print(todoList)

def delete():
  x=input("Enter the task you want to delete from the list: ")
  todoList.remove(x)
  print(todoList)

def modify():
   x=input("Enter the task you want to modify: ")
   if(x in todoList):
      y=input("Enter the new task : ")

      i=todoList.index(x)
      
      todoList[i]=y
      print(todoList)
   else:
      print("The input doesnt match any task in the todo list")

  

add()
while True:
  try: 
      option = int(input("1->Add,2->Delete,3->Modify,4->To see tasks,5->Exit\n Enter the value:\n "))
      if(option==1):
        add()
      elif(option==2):
        delete()  
      elif(option==5):
         print("Final todo list is ",todoList)
         break
      elif(option==3):
         if(len(todoList)>0):
          modify()
         else:
            print("You dont have anything in the todoList to modify")
          
      elif(option==4):
         print(todoList)   
      else:
        print("The value entered was not appropriate")              
  except ValueError:
      print("You should check the correctness of input")
                  

# a=0
# while(a=0): 
  # if(option==1):
  #       add()
  # elif(option==1):
  #       delete()  
  # else:
  #     print("The value entered was not appropriate") 



      
  
    



      


