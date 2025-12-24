userInput= int(input("Enter the number of terms for Fibonacci series: "))

if userInput <= 0:
    print("Please enter a positive integer.")
elif userInput == 1:
    print("Fibonacci series up to", userInput, ":")
    print(0) 
elif userInput == 2:
    print("Fibonacci series up to", userInput, ":")
    print(0, end=",")
    print(1)
else:
    a=0
    b=1
    print("Fibonacci series up to", userInput, ":")
    print(0,b, end=" ")
    for i in range(userInput-2):
        
        print(a+b, end=" ")
        a,b=b,a+b