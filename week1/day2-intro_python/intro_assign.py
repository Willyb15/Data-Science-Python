# my_num = 5
# sum_result = 0
# current = 1
# while current < my_num:
#     sum_result += current
#     current +=1
#     print(current)

# problem 1

# problem 2
# def compare():
#     num1 = int(raw_input("Feed me a number please..."))
#     num2 = int(raw_input("Feed me ANOTHER number please..."))
#     if num1 > num2:
#         print("The first number {0} is larger (>) than the second number {1}").format(num1, num2)
#     elif num1 < num2:
#         print("The first number {0} is smaller (<) than the second number {1}").format(num1, num2)
#         # print('hello')


# problem 3
# def sum_zero():
#     num1 = int(raw_input("Feed me a number please..."))
#     sum = num1 + 0
#     print("This is the sume from zero %s" % sum)
# sum_zero()

# problem 4
# def factorial():
#     num1 = int(raw_input("Feed me a number please..."))
#     count = num1 -1
#     while count > 0:
#         num1*=count
#         count-=1
#         print(num1)
#     print("This is the facotiral total %s" % num1)
# factorial()

# problem 5

# def divisor():
#     dividend = int(raw_input("Feed me a number please..."))
#     divisor = int(raw_input("Feed me a number to divide the first number by please..."))
#     while divisor > 0:
#         if dividend % divisor == 0:
#             print("Dividend is divisiable by %s" % divisor)
#             divisor -=1
#         elif dividend % divisor != 0:
#             print("Dividend is **NOT** divisiable by %s" %divisor)
#             divisor-=1
# divisor()

# problem 6
# def common_divsor():
#     num1 = int(raw_input("Feed me a number please..."))
#     num2 = int(raw_input("Feed me ANOTHER number please..."))
#     start = 0
#     if num1 > num2:
#         start = num2
#     elif num1 < num2:
#         start = num1
#     print("This is the start %s" % start)
#     while start > 0:
#         if num1 % start == 0 and num2 % start == 0:
#             print("This %s is the GCD" % start)
#             return start
#         # else: num1 % start != 0:
#         else:
#             print("This is me decrementing %s" % start)
#             start-=1
# common_divsor()

# problem 7

# def least_common():
#     num1 = int(raw_input("Feed me a number please..."))
#     num2 = int(raw_input("Feed me ANOTHER number please..."))
#     start = 2
#     if num1 > num2:
#         stop = num1
#     else:
#         stop = num2
#     while start < stop:
#         if num1 % start == 0 and num2 % start == 0:
#             print("This %s is the LCD" % start)
#             return start
#         else:
#             print("This is me decrementing %s" % start)
#             start+=1
# least_common()

# problem 8
# prime_numbers = 0
#
# def is_prime_number():
#     num = int(raw_input("Feed me a number please..."))
#     if num >= 2:
#         for y in range(2,num):
#             if num % y == 0:
#                 print(False)
#             else:
#                 print("The number is prinme")
# is_prime_number()


# for i in range(int(raw_input("How many numbers you wish to check: "))):
#     if is_prime_number(i):
#         prime_numbers += 1
#         print i
#
# print "We found " + str(prime_numbers) + " prime numbers."



# def isprime():
#     num = abs(int(raw_input('Feed me a number please')))
#     for i in range(2, num):
#         if num % i == 0:
#             print("The number is not prime yo, its divisible by %d" % i)
#             return
#         else:
#             print('Think we got a prime dawg')
#
# isprime()

def series():
    num = abs(int(raw_input('Feed me a number please')))



















# if __name__ == '__main__':
#     compare()
