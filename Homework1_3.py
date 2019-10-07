print("CALCULATOR")

x = int(input("Enter value for x: "))
y = int(input("Enter value for y: "))

operation = input ("Choose your math operation: ")

if operation == "+":
    print(x+y)
elif operation == "-":
    print (x-y)
elif operation == "*":
    print (x*y)
elif operation == "/":
    print (x/y)
else:
    print("Not a correct operation")
