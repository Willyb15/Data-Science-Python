# Problem 1

# def multiply():
#     num1 = int(raw_input('Type a number'))
#     while num1 < 1:
#         num1 = int(raw_input('your number is negative, enter a positive'))
#     num2 = int(raw_input('Type a number'))
#     while num2 < 1:
#         num2 = int(raw_input('your number is negative, enter a positive'))
#     product = 0;
#     for i in range(0,num2):
#         product+=num1
#         print(product)
#     print("The product is equal to %d" % product)

# multiply()
#
# Problem 2
# def divide():
#     dividend = int(raw_input('Type a number '))
#     while dividend < 1:
#         dividend = int(raw_input('your number is negative, enter a positive'))
#     divisor = int(raw_input('Type a number '))
#     while divisor < 1:
#         divisor = int(raw_input('your number is negative, enter a positive'))
#     quotient = 0;
#     while dividend >= divisor:
#         dividend-=divisor
#         quotient+=1
#         print(quotient)
#     print("The quotient is equal to %d" % quotient)
# divide()

# Problem 3

def expon():
    num1 = int(raw_input('Type a number'))
    while num1 < 1:
        num1 = abs(int(raw_input('your number is negative, enter a positive')))
    num2 = int(raw_input('Type a number'))
    while num2 < 1:
        num2 = abs(int(raw_input('your number is negative, enter a positive')))
expon()
