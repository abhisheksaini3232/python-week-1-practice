"""
Project 4 — Password Strength Checker
Concepts Used:
 Strings, conditions
Features
Minimum length check
Uppercase / lowercase
Numbers & special characters
Display strength: Weak / Medium / Strong

"""

while True:
  password = input("Enter your password to check its strength: ")

  if len(password)<8:
    print("Password is too short, it should be at least 8 characters long.")
  elif  (not any(char.isupper() for char in password)):
    print("Password should contain at least one uppercase letter.")
  elif (not any(char.islower() for char in password)):
    print("Password should contain at least one lowercase letter.")
  elif (not any(char.isdigit() for char in password)):
    print("Password should contain at least one number.")
  elif(all(char.isalnum() or char.isspace() for char in password)):
    print("Password should contain at least one special character.")  
  else:
    print("Your password is strong!")
    break  