while True:
    print("enter 'add' to add two numbers")
    print("enter 'substract to substract two numbers'")
    print("enter 'multiply' to multiply two numbers")
    print("enter 'divide' to divide two numbers")
    print("enter 'quit' to end the program")
    i=input(":")

    if i=="quit":
        break;
    elif i=="add":
        a=float(input("Enter a number"))
        b=float(input("Enter another number"))
        answer=str(a+b)
        print("The answer is"+ answer)
    elif i=="substract":
        a=float(input("Enter a number"))
        b=float(input("Enter another number"))
        answer=str(a-b)
        print("The answer is"+ answer)
    elif i=="multiply":
        a=float(input("Enter a number"))
        b=float(input("Enter another number"))
        answer=str(a*b)
        print("The answer is"+ answer)
    elif i=="divide":
        a=float(input("Enter a number"))
        b=float(input("Enter another number"))
        answer=str(a/b)
        print("The answer is"+ answer)
    else:
        print("Error:wrong input")