# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------
"""-------------Ques- : {write python code for:}------------------------"""
import copy

"""
Input = "aaabaabbceecddd"
Output = a3b1a2b2c1e2c1d3
"""

"""------------------------**************Answer**************************---------------"""

st1="aaabaabbceecddd"

ls=[x for x in st1]
k=ls[0]
a=[]
b=[]
count=0
for i in ls:

    if i!=k:
      a.append(k)
      b.append(count)
      count=1
      k=i
    else:
        count+=1
        k=i
a.append(k)
b.append(count)

print(a,b)
c=""
for i in range(len(a)):
    c=c+a[i]+str(b[i])
print("the result is",c)

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

"""-------------Ques- : {write python code for:}------------------------"""
""" 


Input = ['cat', 'dog', 'fired', 'god', 'pat', 'tap', 'fried', 'tac']
Output = [['cat', 'tac'], ['dog', 'god'], ['fried', 'fired'], ['pat', 'tap']]

"""

"""------------------------**************Answer**************************---------------"""
# ls1=['cat', 'dog', 'fired', 'god', 'pat', 'tap', 'fried', 'tac']
# ls2=[]
#
#
# for i in range(len(ls1)):
#     for j in range(i+1,len(ls1)):
#         if "".join(sorted(ls1[i]))=="".join(sorted(ls1[j])):
#             ls2.append([ls1[i],ls1[j]])
# print(ls2)


##method2:

# input_str = ['cat', 'dog', 'fired', 'god', 'pat', 'tap', 'fried', 'tac']
# sample_str=[]
# output_str=[]
#
# for str1 in input_str:
#   w=[x for x in str1]
#   for i in range(len(w)):
#     for j in range(len(w)):
#       if w[i]<w[j]:
#         w[i],w[j]=w[j],w[i]
#
#   sample_str.append(w)
#
# for i in range(len(sample_str)):
#   for j in range(i+1,len(sample_str)):
#     if sample_str[i]==sample_str[j]:
#       output_str.append([input_str[i],input_str[j]])
#
# print(output_str)


# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------
"""-------------Ques- : {write python code for:}------------------------"""

""" 

Input:
x=['a','b','c','d','e','f','g']
y=[1,2,3] 

Expected output:
[('a',1),('b',2),('c',3),('d',1),('e',2),('f',3),('g',1)]
"""

"""------------------------**************Answer**************************---------------"""
#
# x = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
# y = [1, 2, 3]
#
# z = []
# s = 1
# for i in range(len(x)):
#     if i <= 2:
#         z.append(s)
#     elif i > 2:
#         if z[-1] == 3:
#             z.append(1)
#         elif z[-1] == 2:
#             z.append(3)
#         elif z[-1] == 1:
#             z.append(2)
#
#     s += 1
# print(z)
#
# d=dict(zip(x,z))
# print(list(d.items()))

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------
"""-------------Ques- : {write python code for:}------------------------"""
""" 

Input="i am vignesh k" 

Output='k vignesh am i'
"""

"""------------------------**************Answer**************************---------------"""
# st1="i am vignesh k"
# k=st1.split()
# ls=[]
#
# for i in range(-1,-len(k)-1,-1):
#     ls.append(k[i])
# print(" ".join(ls))


# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------
"""-------------Ques- : {write python code for:}------------------------"""

""" 

write python code for: i have a. dictionary i want to print keys based on values
"""

"""------------------------**************Answer**************************---------------"""


# d={'a':1,'b':2,'c':3,'d':4}
#
# key=list(d.keys())
# val=list(d.values())
# n=int(input("enter a value from {} to obtain the corresponding key".format(val)))
# ind=val.index(n)
# print("the key for the value {} is '{}'".format(n,key[ind]))

# method2


# def value_key(d,n):
#   for i in d:
#     if d[i]==n:
#       print(i)
#
# value_key(d,1)
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------
"""-------------Ques- : {write python code for:}------------------------"""

""" 

Convert a nested list (only nested lists alone)into a flat list:
input:
list_1 = [[14], [215, 383, 87], [298], [374], [2, 3, 4, 5, 6, 7]]
output:
 [14,215,383,87,298,374,2,3,4,5,6,7]

"""

"""------------------------**************Answer**************************---------------"""
# list_1 = [[14], [215, 383, 87], [298], [374], [2, 3, 4, 5, 6, 7]]
# ls2=[]
# for i in list_1:
#     if type(i) is list:
#         for j in i:
#             ls2.append(j)
#
# print(ls2)

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------
"""-------------Ques- : {write python code for:}------------------------"""
"""
create one new list without nested list in input list

input:
list_2 = [1, 23, 45, 67, 89, 11, 12, 13, [3, 4, 5, 6, 7], "atr", "abc"]

output:
[1, 23, 45, 67, 89, 11, 12, 13, "atr", "abc"]
"""
"""------------------------**************Answer**************************---------------"""

# list_2 = [1, 23, 45, 67, 89, 11, 12, 13, [3, 4, 5, 6, 7], "atr", "abc"]
# ls2=[]
#
# for i in list_2:
#     if type(i)!=list:
#         ls2.append(i)
#
# print(ls2)



# -----------------------------------------------------------------------------------------------------------------------
"""-------------Ques- : {write python code for:}------------------------"""
"""
How to find the sub-string count in a given string with overlapping occurrences, 
What that means is if you have a string as mamamea and substring is mam then count is 2.
"""

"""------------------------**************Answer**************************---------------"""

# str1="mamamea"
# count=0
# for i in range(len(str1)):
#     if i<len(str1)-2:
#         if str1[i]+str1[i+1]+str1[i+2]=="mam":
#             count+=1
#
# print("the substring with overlapping occurence is",count)
#


# -----------------------------------------------------------------------------------------------------------------------
"""-------------Ques- : {write python code for:}------------------------"""
"""
How to find the second lowest lists into a nested list by their second value?

Input:

list_1=[['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.20], ['Akriti', 41], ['Harsh', 39]]

output:
second largest mark obtaines by: “Harsh”
"""

"""------------------------**************Answer**************************---------------"""
# list_1=[['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.20], ['Akriti', 41], ['Harsh', 39]]
#
# name=[]
# val=[]
#
# for i in range(len(list_1)):
#     name.append(list_1[i][0])
#     val.append(list_1[i][1])
# val1=copy.deepcopy(val)
# val1.sort()
# print(val1,name,val)
# sec_large=val1[-2]
# ind=val.index(sec_large)
# print("name with second largest number is",name[ind])

##method-2 for second lowest:

# list_1 = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.20], ['Akriti', 41], ['Harsh', 39]]
# name = [list_1[x][0] for x in range(len(list_1))]
# mark = [list_1[x][1] for x in range(len(list_1))]
# first_lowest = mark[0]
# second_lowest = mark[1]
#
# for i in range(len(mark)):
#     if mark[i] < first_lowest:
#         second_lowest = first_lowest
#         first_lowest = mark[i]
#
#     elif mark[i] < second_lowest and mark[i] != first_lowest:
#         second_lowest = mark[i]
#
# print(first_lowest, second_lowest)
# second_lowest_name = []
# for i in range(len(mark)):
#     if mark[i] == second_lowest:
#         second_lowest_name.append(name[i])
#
# print(name, mark, second_lowest_name)

# -----------------------------------------------------------------------------------------------------------------------
"""-------------Ques- : {write python code for:}------------------------"""

"""
Write a program which takes two strings as input from the user (str1 and str2). This program should print two strings as output (op1 and op2).
op1 should contain all the characters which are present in str1 but NOT present in str2.
op2 should contain all the characters which are present in str2 but NOT present in str1.

For example:
                str1	str2	op1	op2
    Example 1	ABC	    BC	    A	<null>
    Example 2	BC	BANGALORE	C	ANGLORE
    """

"""------------------------**************Answer**************************---------------"""
# st1=input("enter the string")
# st2=input("enter the another string")
# ls_st1=[x for x in st1]
# ls_st2=[x for x in st2]
# op1=[]
# op2=[]
# print(ls_st1,ls_st2)
# for i in ls_st1:
#     if i not in ls_st2:
#         if i not in op1:
#             op1.append(i)
# print("".join(op1))
#
# for i in ls_st2:
#     if i not in ls_st1:
#         if i not in op2:
#             op2.append(i)
# print("".join(op2))
#



# -----------------------------------------------------------------------------------------------------------------------
"""-------------Ques-: {write python code for:}------------------------"""

"""
An array (or list or equivalent) F1 has got names of Facebook users and their friend association.
For example, if we write:  User1, User2 it implies that User1 is a friend of User2. 
This also implies that User2 is a friend of User1.
Write a program which will parse F1 and remove duplicates and write all the unique pairs to a new array F2.

For example, the array F1 might have the following data:

U1,U2
U3,U4
U1,U5
U2,U1
U3,U4

Array F2 should now have:
U1,U2
U3,U4
U1,U5
"""

"""------------------------**************Answer**************************---------------"""
#
# f1=[["U1","U2"],["U3","U4"],["U1","U5"],["U2","U1"],["U3","U4"]]
# f2=[]
#
# for i in f1:
#     f2.append(sorted(i))
# print(f2)
# f3=[]
# for i in f2:
#     if i not in f3:
#         f3.append(i)
# print("The output is",f3)

#method2:
# f1=[["U1","U2"],["U3","U4"],["U1","U5"],["U2","U1"],["U3","U4"]]
#
# def sort_x(x):
#
#   for i in range(len(x)):
#     for j in range(len(x)):
#       if x[i]<x[j]:
#         x[i],x[j]=x[j],x[i]
#
#   return x
#
# f2=[]
#
# for i in f1:
#   f2.append(sort_x(i))
#
# f3=[]
# for i in f2:
#   if i not in f3:
#     f3.append(i)
#
# print(f3)


# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------
"""-------------Ques- : {write python code for:}------------------------"""
"""
create one new list with moved zeroes to the end

input:
list_2 = [1,23,0,45,0,67,0,89,0,11,0,12,0,13,0]

output:
[1, 23,45,67,89,11,12,13,0,0,0,0,0,0,0]

"""
"""------------------------**************Answer**************************---------------"""
# list_2 = [1,23,0,45,0,67,0,89,0,11,0,12,0,13,0]
# ls1=[]
# ls2=[]
#
# for i in list_2:
#     if i==0:
#         ls1.append(i)
#     else:
#         ls2.append(i)
# ls2.extend(ls1)
# print("The output is",ls2)


"""pyramid pattern"""

# def pyramid(n):
#
#     for i in range(n):
#         for j in range(n-i):
#             print(" ",end="")
#         for j in range(i+1):
#             print("*", end=" ")
#
#         print()
# pyramid(5)