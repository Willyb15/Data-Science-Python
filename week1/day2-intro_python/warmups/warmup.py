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
    print("The product is equal to %d" % product)

# multiply()
#
# Problem 2
def divide():
    dividend = int(raw_input('Type a number '))
    while dividend < 1:
        dividend = int(raw_input('your number is negative, enter a positive'))
    divisor = int(raw_input('Type a number '))
    while divisor < 1:
        divisor = int(raw_input('your number is negative, enter a positive'))
    quotient = 0;
    while dividend >= divisor:
        dividend-=divisor
        quotient+=1
        print(quotient)
    print("The quotient is equal to %d" % quotient)
divide()

# Problem 3

def pow():
    a = int(raw_input('Type a number'))
    while a < 1:
        a = abs(int(raw_input('your number is negative, enter a positive')))
    b = int(raw_input('Type a number'))
    while b < 1:
        b = abs(int(raw_input('your number is negative, enter a positive')))
    if(b==0):
        return 1
    answer=a;
    increment=a;
    for i in range(1,b):
        for j in range(1,a):
            answer+=increment
        increment+=answer
        print('pow %d' %answer)
pow()
