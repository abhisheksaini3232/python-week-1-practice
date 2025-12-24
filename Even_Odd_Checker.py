while True:
  try:
    value=int(input("Input a number to check even or odd: "))
    if value%2==0:
        print(f"{value} is Even")  
    else:
        print(f"{value} is Odd")
  except ValueError:
      print("Please enter a valid integer.")        