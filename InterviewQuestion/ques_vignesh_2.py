"""1.Write a function that takes a list of integers as input and returns
the two largest integers in the list."""

# def two_largest(ls):
#     for i in range(len(ls)):
#         for j in range(len(ls)):
#             if ls[i]<ls[j]:
#                 ls[i],ls[j]=ls[j],ls[i]
#
#     print("the 2 largest numbers in the provided list is",ls[-2:])
#
# n=int(input("enter the number of integers that you would like to add it to the list"))
# ls1=[]
# for i in range(n):
#     p=int(input("enter the number"))
#     ls1.append(p)
#
# two_largest(ls1)
#

"""2.Write a function that takes a list of strings as input and returns the shortest string that 
contains all the characters in the list."""

# ls1=["strings","that", "can","have","some","stings"]



"""3.Write a function that takes two strings as input and returns the number of characters that are
 different between the two strings."""

# def string_difference(string1,string2):
#     s1=[x for x in string1]
#     s2=[x for x in string2]
#     s1=set(s1)
#     s2=set(s2)
#     print("The difference between two string are the following characters",list(s1.difference(s2))+list(s2.difference(s1)))
#
#
# st1="happening"
# st2="happiness"
# string_difference(st1,st2)

"""4.Write a function that takes a list of integers as input and returns a new list containing 
only the even numbers from the input list, in the same order."""

# def even_list(ls):
#     ls1=[]
#     for i in ls:
#         if i%2==0:
#             ls1.append(i)
#     print(ls1)
#
# lst=[2,5,3,8,7,1,4,6]
#
# even_list(lst)

"""5.Write a function that takes a string as input and returns a new string where each character is 
replaced by its corresponding ASCII code."""

# def ascii_code(st):
#     s=""
#     for i in st:
#         s=s+" "+str(ord(i))
#     print(s)
#
# str1="Welcome"
# ascii_code(str1)

"""6.Write a function that takes a list of integers as input and returns a new list where each element 
is the sum of the corresponding element in the input list and its two neighbors. For example, if the 
input list is [1, 2, 3, 4], the output list would be [3, 6, 9]."""

# def sum_with_neighbours(ls):
#     n=len(ls)
#     ls1=[]
#     for i in range(n):
#         if i==0:
#             s=ls[i]+ls[i+1]
#         elif i==n-1:
#             s=ls[-1]+ls[-2]
#         else:
#             s=ls[i-1]+ls[i]+ls[i+1]
#         ls1.append(s)
#     print(ls1)
#
# ls=[1,2,3,4]
#
# sum_with_neighbours(ls)
#
#

"""7.Write a function that takes a string as input and returns a new string where each word in the input string 
is reversed, but the order of the words is the same. For example, if the input string is "hello world", 
the output string would be "olleh dlrow"."""

# def word_reverse(string):
#     s = ""
#     ls = string.split()
#     ls1 = []
#     for i in ls:
#         for j in range(len(i)):
#             s = i[j] + s
#         ls1.append(s)
#         s = " "
#     print(" ".join(ls1))
#
# st="hello world"
#
# word_reverse(st)



"""8.Write a function that takes a list of strings as input and returns a new list where each element is a
 string containing the first letter of each word in the corresponding input string. For example, if the input 
 list is ["hello world", "python is cool"], the output list would be ["hw", "pic"]."""

# def first_char_pick(ls):
#     ls2 = []
#     for i in ls:
#         s = i.split()
#         w = ""
#         for j in s:
#             w = w + j[0]
#         ls2.append(w)
#
#     print(ls2)
#
#
# ls1=["hello world", "python is cool"]
#
# first_char_pick(ls1)

"""9.Write a function that takes a list of integers as input and returns a new list where each element 
is the product of all the elements in the input list except for the corresponding element. 
For example, if the input list is [1, 2, 3, 4], the output list would be [24, 12, 8, 6]."""

# def multi_neigh(ls):
#     ls1 = []
#     for i in range(len(ls)):
#         p = 1
#         for j in ls:
#             p = p * j
#         ls1.append((p / ls[i]))
#     print(ls1)
#
# lst=[1,2,3,4]
# multi_neigh(lst)



"""10.Write a function that takes a string as input and returns a new string where each character is replaced
 by the character that appears next to it in the alphabet. For example, if the input string is "hello", 
 the output string would be "ifmmp"."""

# def next_char(str):
#     w = ""
#     for i in str:
#         w = w + chr(ord(i) + 1)
#
#     print(w)

#
# str="hello"
# next_char(str)
