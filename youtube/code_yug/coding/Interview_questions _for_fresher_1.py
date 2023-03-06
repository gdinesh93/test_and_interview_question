"""1.write a program to swap 2 numbers"""
import time

# a = 20
# b = 32
# a, b = b, a
# print("the value of a is ", a)
# print("the value of b is", b)

"""2.reverse string using for loop"""
# string_1 = "welcome"
# rev_string = ""
#
# for i in string_1:
#     rev_string = i + rev_string
#
# print("the reversed string is, ", rev_string)

"""3.reverse string using slicing"""

# string_1 = "welcome"
# rev_string = string_1[::-1]

# print("the reversed string is, ", rev_string)

"""4.chek whether the number is prime"""

#
# def prime(n):
#     if n > 1:
#         count = 0
#         for i in range(1, n + 1):
#             if n % i == 0:
#                 count += 1
#         if count == 2:
#             print("the number is prime")
#         else:
#             print("the number is not prime")
#
#
# prime(5)


"""5.print the prime numbers between the range"""

# def prime(n,m):
#     for i in range(n,m+1):
#         if i>1:
#             for j in range(2,i):
#                 if i%j==0:
#                     break
#             else:
#                 print(i)
#
# prime(1,50)


"""6.menu driven program for calculator"""

# while True:
#     num_1 = int(input("enter the first number"))
#     num_2 = int(input("enter the second number"))
#     print("1.Addition\n2.Subtraction\n3.Multiplication\n4.Division")
#     method = int(input("choose from above option"))
#     if method == 1:
#         print("the addition of {} and {} is {}".format(num_1, num_2, num_1 + num_2))
#     elif method == 2:
#         print("the subtraction of {} and {} is {}".format(num_1, num_2, num_1 - num_2))
#     elif method == 3:
#         print("the multiplication of {} and {} is {}".format(num_1, num_2, num_1 * num_2))
#     elif method == 4:
#         print("the division of {} and {} is {}".format(num_1, num_2, num_1 / num_2))
#     else:
#         print("the option is wrong")
#     cont = input("do you wish to continue?(y/n)")
#     if cont.lower() == "n":
#         print("thank you")
#         break

""""""
