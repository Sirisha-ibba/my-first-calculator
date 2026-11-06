while True:
    print("\n--- Calculator ---")
    print("Type 'exit' to stop")

    num1=input("Enter first number:")
    if num1 =="exit":
        print("Bye! Calculator closed")
        break

    num2=input("Enter second number:")
    op=input("Enter + - * / :")

    num1=float(num1)
    num2=float(num2)

    if op=="+":
        print("Result:", num1+num2)
    elif op=="-":
        print("Result:", num1-num2)
    elif op=="*":
        print("Result:", num1*num2)
    elif op=="/":
        if num2==0:
            print("Error! Cannot divide by zero!")
        else:
            print("Result:", num1/num2)
    else:
        print("Ivalid operator")