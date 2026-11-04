a = int(input("Enter a value:"))
b = int(input("Enter b value:"))
oper = input("Enter a operation (+, -, *, /):")
if oper == "+":
   print(a+b)
elif oper == "-":
   print(a-b)
elif oper == "*":
   print(a*b)
elif oper == "/":
    if b==0:
        print("Cannot divided by zero!")
    else:
        print(a/b)
else:
    print("Invalid operation")
        
