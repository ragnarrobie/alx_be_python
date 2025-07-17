num1 = int(input("Enter the first number:"))
num2 = int(input("Enter the second number:"))
operation = input("choose the operation (+,-,*,/):")
sum = num1 + num2
product= num1*num2
difference = num1-num2

match operation:
    case "+":
        print("The result is", sum)
    case "-":
        print("The difference is", difference)
    case "*":
        print("The product is", product)
    case "/":
        if num2==0:
         print("Cannot divide by zero")
        else:
            quotient = num1/num2
            print("The quotient is", quotient)
    case _:
        print("invalid operation")
        
    
        