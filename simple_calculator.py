# A simple Calculator
printf("Welcome to a simple calculator")

operation = input(" Choose an operation to perform. Add, subtract, multiplication or division? ")

#user chooses his two numbers
num1 = float(input("Insert your first number "))

num2 = float(input("Insert your second number "))



if operation == "add":
    sum = num1 + num2
    print("Answer is " + str(sum))

elif operation == "subtract":
    diff = num1 - num2
    print("Answer is " + str(diff))

elif operation == "multiplication":
    product = num1 * num2
    print("Answer is " + str(product))

elif operation == "division":
    quotient = num1 / num2
    print("Answer is " + str(quotient))
