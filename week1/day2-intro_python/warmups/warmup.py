# Problem 1

def multiply():
    num1 = int(raw_input('Type a number'))
    while num1 < 1:
        num1 = int(raw_input('your number is negative, enter a positive'))
    num2 = int(raw_input('Type a number'))
    while num2 < 1:
        num2 = int(raw_input('your number is negative, enter a positive'))
    product = 0;
    for i in range(0,num2):
        product+=num1
        print(product)
multiply()
