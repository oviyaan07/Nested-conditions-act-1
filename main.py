medc=input("Do you have a medical cause(Y/N)")
if medc=='Y'or medc=='y':
    print("you are allowed to write the exam")
elif medc=='N' or medc=='n':
    per=float(input("enter your attendence percentage"))
    if per>=75:
        print("you are allowed to write the exam")
    else:
        print("you are not allowed to write the exam")
else:
    print("please enter valid input")