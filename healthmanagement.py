import datetime
def gettime():
    return datetime.datetime.now()
def take(k):
    if k==1:
        d= int(input("Type 1 for Exercise and 2 for Diet:"))
        if d==1:
            value= input("Type here")
            with open ("sam.txt","a") as op:
                op.write(str(gettime())+":"+value)
            print("Entered Successfully")
        elif d==2:
            value = input("Type here")
            with open("sam1.txt", "a") as op:
                op.write(str(gettime()) + ":" + value)
            print("Entered Successfully")
    elif k==2:
        d = int(input("Type 1 for Exercise and 2 for Diet:"))
        if d==1:
            value= input("Type here")
            with open ("rohan.txt","a") as op:
                op.write(str(gettime())+":"+value)
            print("Entered Successfully")
        elif d == 2:
            value = input("Type here")
            with open("rohan1.txt", "a") as op:
                op.write(str(gettime()) + ":" + value)
            print("Entered Successfully")
    elif k==3:
        d = int(input("Type 1 for Exercise and 2 for Diet:"))
        if d == 1:
            value = input("Type here")
            with open("hammad.txt", "a") as op:
                op.write(str(gettime()) + ":" + value)
            print("Entered Successfully")
        elif d == 2:
            value = input("Type here")
            with open("hammad1.txt", "a") as op:
                op.write(str(gettime()) + ":" + value)
            print("Entered Successfully")
def retrieve(b):
    if b==1:
        c = int(input("Type 1 for Exercise and 2 for Diet:"))
        if c==1:
            with open("sam.txt") as op:
                for i in op:
                    print(i, end=" ")
        elif c==2:
            with open("sam1.txt") as op:
                for i in op:
                    print(i, end=" ")
    if b==2:
        c = int(input("Type 1 for Exercise and 2 for Diet:"))
        if c==1:
            with open("rohan.txt") as op:
                for i in op:
                    print(i, end=" ")
        elif c==2:
            with open("rohan1.txt") as op:
                for i in op:
                    print(i, end=" ")
    if b==3:
        c = int(input("Type 1 for Exercise and 2 for Diet:"))
        if c==1:
            with open("hammad.txt") as op:
                for i in op:
                    print(i, end=" ")
        elif c==2:
            with open("hammad1.txt") as op:
                for i in op:
                    print(i, end=" ")

hello= int(input("Enter 1 if you want to log and 2 if you want to retrieve :"))
if hello==1:
    a= int(input("Enter 1 for Harry, 2 for Rohan and 3 for Hammad  "))
    take(a)
elif hello==2:
    c= int(input("Enter 1 for Harry, 2 for Rohan and 3 for Hammad  "))
    retrieve(c)
else:
    print("Invalid Input!")