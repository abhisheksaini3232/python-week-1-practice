n=int(input("Write n for pattern : "))
a=bool(input("Give True or False: "))
if(a==True):
    for i in range(n,0,-1):
        print(i* "*")
        n=n-1
elif(a==False):
        for i in range(n,0,-1):
            print(i* "*")
            n=n-1