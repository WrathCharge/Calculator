num1 = int(input("Enter a number:\n"))
op = input("Select an operator.\n")
num2 = int(input("Enter a number:\n"))
while True:
    if op == "+":
        add = num1 + num2
        print("Answer:", add)
    elif op == "-":
        sub = num1 - num2
        print("Answer:", sub)
    elif op == "*":
        mul = num1 * num2
        print("Answer:", mul)
    elif op == "/":
        div = num1 / num2
        print("Answer:", div)
    elif op == "**":
        pov = num1 ** num2
        print("Answer:", pov)
    i = input("Do you want to continue?")
    if i == "Yes":
        continue
    elif i == "yes":
        continue
    else:
        break
    
