"""1.find the second lowest grade and the name of the student"""

# list_1=[['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.20], ['Akriti', 41], ['Harsh', 39]]

# second lowest - tina
# name=[]
# val=[]
#
# for i in range(len(list_1)):
#     name.append(list_1[i][0])
#     val.append(list_1[i][1])
# val1=[]
# for i in val:
#     val1.append(i)
#
# #sorting
# for i in range(len(val1)):
#     for j in range(len(val1)):
#         if val1[i]<val1[j]:
#             val1[i],val1[j]=val1[j],val1[i]
#
# mini=val1[0]
# min_diff=val1[1]-mini
#
# for i in range(len(val1)):
#     for j in range(i+1,len(val1)):
#         if val1[i]-mini<min_diff and val1[i]-mini!=0:
#             min_diff=val1[i]-mini
# sec_lowest=mini+min_diff
# print(list_1)
# print("the second lowest grade value is",sec_lowest)
# for i in range(len(val)):
#     if val[i]==sec_lowest:
#         print("the student with second ",name[i])

# def second_lowest(ls):
#     name = []
#     val = []
#
#     for i in range(len(ls)):
#         name.append(ls[i][0])
#         val.append(ls[i][1])
#     d = dict(zip(name, val))
#
#     for i in range(len(val)):
#         for j in range(len(val)):
#             if val[i] < val[j]:
#                 val[i], val[j] = val[j], val[i]
#
#     for i in range(len(val)):
#         if val[i] != val[0]:
#             scnd_low = val[i]
#             break
#     for i in name:
#         if d[i] == scnd_low:
#             print("the student '{}' has got the second lowest grade {}".format(i, d[i]))
#
#
# second_lowest(list_1)

# list_1 = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.20], ['Akriti', 41], ['Harsh', 39]]

# def second_lowest(ls):
#     d = {}
#     val=[]
#     for i in range(len(list_1)):
#         grade = list_1[i][1]
#         name = list_1[i][0]
#         if list_1[i][1] not in d:
#             d[grade] = name
#             val.append(grade)
#         else:
#             d[grade] = list((d[grade], name))
#
#     for i in range(len(val)):
#         for j in range(len(val)):
#             if val[i] < val[j]:
#                 val[i], val[j] = val[j], val[i]
#
#     print("the second lowest grade is {} and the scorer(s) is/are {}".format(val[1],d[val[1]]))
#
# second_lowest(list_1)

"""2.alternative prime number"""
#
# def alt_prime(n,m):
#     count=0
#     list_prime=[]
#     for i in range(n,m+1):
#         if i>1:
#             for j in range(2,i):
#                 if i%j==0:
#                     break
#             else:
#                 if count%2==0:
#                     list_prime.append(i)
#                 count += 1
#     print(list_prime)
# alt_prime(1,50)

"""3.function for sort and count"""
# def Sort(ls):
#     for i in range(len(ls)):
#         for j in range(len(ls)):
#             if ls[i]<ls[j]:
#                 ls[i],ls[j]=ls[j],ls[i]
#
#     return ls
# ls1=[3,2,11,9,6,23,2,2,2]
# print(Sort(ls1))
#
# def list_count(ls):
#     count_dic={}
#     for i in ls:
#         iter_count = 0
#
#         for j in ls:
#             if i==j:
#                 iter_count+=1
#         count_dic[i]=iter_count
#     return count_dic

# print("the count of 2 in the list is",list_count(ls1))

"""4.second maximum number in the list"""

# ls=[3,5,2,6,1,9,8,7,10]
# first_max=ls[1]
# second_max=ls[2]
#
# for i in ls:
#   if i>first_max:
#     second_max=first_max
#     first_max=i
#   elif i>second_max:
#     second_max=i
#
# print(first_max,second_max)

"""5.return the list of number that is power of 2 between the range"""

# def power_of_two(low_range,upper_range):
#     list_1 = []
#     for i in range(low_range,upper_range+1):
#         n = i
#         if n % 2 == 0:
#             while True:
#                 n = n / 2
#                 if n == 1:
#                     list_1.append(i)
#                 if n < 1:
#                     break
#     return list_1
#
# print(power_of_two(0,100))
#

# val=[2,4,6,3,5,6,8,8]
# max=val[0]
# for i in range(len(val)):
# 	if val[i]>max:
# 		max=val[i]
# min_diff=max-val[0]
# for i in range(len(val)):
#     if max-val[i]<min_diff and max-val[i]!=0:
#         min_diff=max-val[i]
#
# print("second largest number is,", max - min_diff)

"""6.
            indium L2
str1="wwwindiumsoft"
#output=w3i2n1d1u1m1s1o1f1t1

"""
# str1="wwwindiumsoft"
#
# d={}
#
# for i in str1:
# 	if i not in d:
# 		d[i]=1
# 	else:
# 		d[i]+=1
#
# output_str=""
#
# for i in d:
# 	output_str=output_str+i+str(d[i])
#
# print("The output string with the character occurrence is",output_str)

"""7.           indium L2
#A1[] = {2, 1, 2, 5, 7, 1, 9, 3, 6, 8, 8} A2[] = [2, 1, 8, 3] Output: 2 2 1 1 8 8 3 3 5 6 7 9
"""
#
# list_1 = [2, 1, 2, 5, 7, 1, 9, 3, 6, 8, 8]
# list_2 = [2, 1, 8, 3]
# list_3=[]
# list_4 = []
#
# for i in list_2:
#     if i in list_1:
#         list_3.extend([i, i])
#         list_1.remove(i)
#
# for i in list_1:
#     if i not in list_2:
#         list_4.append(i)
#
# list_4.sort()
# list_3.extend(list_4)
# print("The output list is", list_3)

""""8. mock by vicki l=[1,2,3,None,4,5,None,6,None,7,8] outpu=[1,2,3,3,4,5,5,6,6,7,8]"""

# list_1=[1,2,3,None,4,5,None,6,None,7,8]
# output_list=[]
# for i in list_1:
# 	if i:
# 		output_list.append(i)
# 	else:
# 		output_list.append(output_list[-1])
# print(output_list)

"""9. mock by vicki reverse the given float num=123.345 output=321.543"""
#
# num=123.345
# list_1=str(num).split(".")
# str1=""
# op_list=[]
# for i in list_1:
# 	for j in i:
# 		str1=str(j)+str1
# 	op_list.append(str1)
# 	str1=""
# print("the output is ,",".".join(op_list))
#

"""10, mindteck l1
 str1="python" str2="pythoon" output="o" """
# str1="python"
# str2="pythoon"
# list_1=[x for x in str1]
# list_2=[x for x in str2]
#
# for i in list_1:
# 	if i in list_2:
# 		list_2.remove(i)
#
# print("the remaining char is,=",list_2)

"""11, mindtek l1
count the word occurrence and print the word that has been repeated more than once = str1="python is robust framework and python is pytest"

"""

# str1 = "python is robust framework and python is pytest"
# d = {}
# list1 = str1.split()
#
# for i in list1:
#     if i.lower() not in d:
#         d[i] = 1
#     else:
#         d[i] += 1
#
# rep_list = []
#
# for i in d:
#     if d[i] > 1:
#         rep_list.append(i)
#
# print("the word occurrence in the given string is", d)
# print("the repeated word occurrence in the given string is", rep_list)

"""12, str1="today I have the python interview" reverse the arrangement of the word
"""
# str1="today I have the python interview"
# list_1=str1.split()
# list_2=[]
# for i in range(-1,-len(list_1)-1,-1):
#   list_2.append(list_1[i])
#
# print("The reversed word is ="," ".join(list_2))

"""13,sort the list"""

# list1=[3,10,20,100,80]
#
# for i in range(len(list1)):
#   for j in range(len(list1)):
#     if list1[i]<list1[j]:
#       list1[i],list1[j]=list1[j],list1[i]
#
# print("the sorted list is", list1)

"""14. MINDTECH L2
check the move of rook in chess initial position is x, y = "b", 2 desired position are as follows-
x1, y1 = "b", 8 have to give valid move as output
x1,y1="a",10 have to give invalid move as output
"""
# x, y = "b", 2
# x1, y1 = "b", 8
# # x1,y1="a",10
# def rook_move_check(initial_x, initial_y, dest_x, dest_y):
#     if dest_x <= "h" and dest_y <= 8:
#         if dest_x == initial_x or dest_y == initial_y:
#             print("the move is valid, and the rook moves to '{}{}'".format(dest_x,dest_y))
#
#         else:
#             print("the move is invalid, try another move")
#     else:
#         print("not the legal move, try to be within the board boundary")
#
# rook_move_check(x, y, x1, y1)

"""15. synchetron 
reverse the string using the while loop"""

# str1="dinesh"
# output_str=""
# count=0
# while True:
#     if len(output_str)==len(str1):
#         break
#     else:
#         output_str=str1[count]+output_str
#         count+=1
#
# print(output_str)

"""16. Logitech

remove the suffixes ("ed","ly", "ing") from the words given in the string and if the length of the word is greater 
than 8 strip it to 8 letter word"""

# str1 = "he is lying on the floor concussioned with the straped legs fully enclosed"
#
# def strammer(str1):
#     list_str = str1.split()
#     print(list_str)
#     new_list = []
#     for i in list_str:
#         if len(i) <= 8:
#             if i[len(i) - 2:] == "ed" or i[len(i) - 2:] == "ly":
#                 new_str = i[:len(i) - 2]
#
#             elif i[len(i) - 3:] == "ing":
#                 new_str = i[:len(i) - 3]
#
#             else:
#                 new_str = i
#
#         else:
#             new_str = i[:8]
#         new_list.append(new_str)
#
#     print(" ".join(new_list))
#
#
# strammer(str1)

"""17. Logitech
get the list of integers from the user and sort it in ascending order and 
find the sum of difference of adjacent elements in the list, if the sum is even return true and the 
sum and if sum is odd return false and the sum value"""
#
# def list_even_validation(list1):
#
#   #sorting the list
#   for i in range(len(list1)):
#     for j in range(len(list1)):
#       if list1[i]<list1[j]:
#         list1[i],list1[j]=list1[j],list1[i]
#
#   #finding the difference with the adjacent element
#   new_list=[]
#   for i in range(len(list1)):
#     if i<len(list1)-1:
#       diff=list1[i+1]-list1[i]
#     new_list.append(diff)
#
#   #finding the sum of difference of adjacent element list
#   sum=0
#   for i in new_list:
#     sum=sum+i
#   if sum%2==0:
#     print("the sum of the difference of adjacent element is {} and it is even.".format(sum))
#   else:
#     print("the sum of the difference of adjacent element is {} and it is odd.".format(sum))
#
# n=int(input("enter the number of elements in a list"))
# user_list=[]
# for i in range(n):
#   p=int(input("enter the element to be added in the list"))
#   user_list.append(p)
#
# list_even_validation(user_list)
#
#
"""18. bracket validation"""
# a = "({[]})"
# open_brack = ["(", "{", "["]
# close = [")", "}", "]"]
# list_para = []
# count_open = 0
# count_close = 0
# for i in a:
#     if i not in close:
#         list_para.append(i)
#         count_open += 1
#     else:
#         try:
#             count_close += 1
#             if list_para[-1] == open_brack[close.index(i)]:
#                 list_para.pop()
#         except:
#             pass
# if list_para:
#     print("this is not valid")
#
# else:
#     if count_open == count_close:
#         print("this is valid set")
#     else:
#         print("this is not valid set")

"""single bracket"""
# a = "((())))))"
# list_para = []
# count_open = 0
# count_close = 0
# for i in a:
#     if i != ")":
#         list_para.append(i)
#         count_open += 1
#     else:
#         try:
#             count_close += 1
#             list_para.pop()
#         except:
#             pass
# if list_para:
#     print("this is not valid")
#
# else:
#     if count_open == count_close:
#         print("this is valid set")
#     else:
#         print("this is not valid set")

"""19.Indium L3"""

# list_num=[1,2,3,4,5,6]
# num=8
# output_list=[] #[[2, 6], [3, 5], [1, 2, 5], [1, 3, 4]]

# for i in range(len(list_num)):
#   for j in range(i+1,len(list_num)):
#     if list_num[i]+list_num[j]==num:
#       output_list.append([list_num[i],list_num[j]])


# for i in range(len(list_num)):
#   for j in range(i+1,len(list_num)):
#     for k in range(j+1,len(list_num)):
#       if list_num[i]+list_num[j]+list_num[k]==num:
#         output_list.append([list_num[i],list_num[j],list_num[k]])

# print(output_list)


"""20. Indium L3"""
# A1[] = {2, 1, 2, 5, 7, 1, 9, 3, 6, 8, 8} A2[] = [2, 1, 8, 3] Output: 2 2 1 1 8 8 3 5 6 7 9
# list_1=[2, 1, 2, 5, 7, 1, 9, 3, 6, 8, 8]
# list_2=[2, 1, 8, 3]
# output_list=[]
# temp_dic={} #{2: 2, 1: 2, 5: 1, 7: 1, 9: 1, 3: 1, 6: 1, 8: 2}
#
# for i in list_1:
#   if i not in temp_dic:
#     temp_dic[i]=1
#   else:
#     temp_dic[i]+=1
#
# print(temp_dic)
#
# for i in list_2:
#   if i in temp_dic:
#     for j in range(temp_dic[i]):
#       output_list.append(i)
# # print(output_list)
#
# list_3=[]
#
# for i in list_1:
#   if i not in list_2:
#     list_3.append(i)
#
# # print(list_3)
#
# list_3.sort()
# output_list.extend(list_3)
# print("the output is =",output_list)

"""21.Mindtech L3"""

# # Input = [-6,-4,1,2,3,5]
# # Output = [36, 25, 16, 9, 4, 1]

# list_input= [-6,-4,1,2,3,5]
# list_temp=[]

# for i in list_input:
#   if i <0:
#     list_temp.append(i*(-1))
#   else:
#     list_temp.append(i)
# # print(list_temp)

# # sorting the list:ls=[4,2,3,1]
# for i in range(len(list_temp)):
#   for j in range(len(list_temp)):
#     if list_temp[i]>list_temp[j]:
#       list_temp[i], list_temp[j]=list_temp[j], list_temp[i]

# # print(list_temp)

# #squaring the list element:
# list_output=[]
# for i in list_temp:
#   list_output.append(i*i)

# print("the output is ", list_output)

"""22. Mindtech L3"""

# string_1="helloworld"

# N = 6
# Output : hellodliow
# n=6
# string_temp=""
# count=1
# for i in string_1:
#   if count<n:
#     string_temp+=i
#   else:
#     string_temp+=chr(122-ord(i)+97)
#   count+=1
# print(string_temp)

"""23. Msys L1"""
# operations
#
#
# class A:
#     def add(self, a, b):
#         print(a + b)
#
#     def sub(self, a, b):
#         print(a - b)
#
#
# from operations import A
#
# a = int(input("enter the number"))
# b = int(input("enter another number"))
#
# obj_a = A()
# obj_a.add(a, b)
# obj_a.sub(a, b)

"""24. Msys L1"""
# get the list and pass it into the method and remove the provided element.

# def element_removal(ls, ele):
#     count = 0
#     for i in ls:
#         count += 1
#         if i == ele:
#             ls.remove(i)
#             print("the list after the removed element is {} and the element is removed from the index {}".format(ls,
#                                                                                                                  count - 1))
#
#             break
#     else:
#         print("the given number is not in the list")
#
#
# n = int(input("enter the number of elements that you would like in the list"))
# list_1 = []
# for i in range(n):
#     a = int(input("enter the element"))
#     list_1.append(a)
#
# b = int(input("enter the number that you would like to be removed"))
#
# element_removal(list_1, b)

"""25. synechron L2"""

# n=13
# # 1,10,11,12,13=6
# list_1=[x for x in range(1,n+1)]
# count=0
# for i in list_1:
#   str_num=str(i)
#   for j in str_num:
#     if j=="1":
#       count+=1
# print("the count of 1 in the range of 13 is", count)

"""26. Msys L2"""

# statement = "Python for call interview an is This"
#
# list_temp=statement.split()
#
# output_statement=[]
#
# for i in range(-1, -(len(list_temp)+1), -1):
#   output_statement.append(list_temp[i])
#
# print("the reversed statement is= ", " ". join(output_statement))

"""27. Msys L2"""

# def triangle(n):
#   for i in range(n):
#     for j in range(n-i):
#       print(" ", end="")
#     for j in range(i+1):
#       print("*", end=" ")
#     print()
#
# triangle(5)

"""28. Msys L2"""

# factorial of 6 using recursive

# def fact(n):
#   if n==0 or n==1:
#     return n
#   else:
#     return n*fact(n-1)
#
# print(" The factorial is ",fact(6))

"""29. Msys L2"""

# mystring="asbsdflwerbsdf9erj;ladsfvnasldfkwierhWALKJ"
#
# count=0
#
# for i in mystring:
#   if i.lower()=="a":
#     count+=1
#
# print("the number of occurrence of the letter a is =", count)


"""30. Msys L2"""

# def prime():
#   i=2
#   while True:
#     if i>1:
#       for j in range(2,i):
#         if i%j==0:
#           break
#       else:
#         yield i
#       i+=1
#
# f=prime()
#
# for i in prime():
#   print(i)


"""31. Msys L2"""

# list1 = [11, 22, 5, 46, 98, 57,64, 43, 2, 36,90]
#
# first_largest=list1[0]
# second_largest=list1[1]
#
# for i in range(len(list1)):
#   if list1[i]>first_largest:
#     second_largest=first_largest
#     first_largest=list1[i]
#
#   elif list1[i]>second_largest:
#     second_largest=list1[i]
#
# print("the second largest number is, ", second_largest)

"""32. Msys L2"""

# class Test_fullname:
#     first = "dinesh"
#     last = "murugan"
#     name = "dinesh murugan"
#
#     @pytest.mark.name
#     def test_combine(self):
#         temp_fullname = self.fname + " " + self.lname
#         assert self.name == temp_fullname

"""33.Msys L2"""

import re
import subprocess

content=subprocess.run("ipconfig", capture_output=True)
text=str(content.stdout)
p=re.compile(r"(?<=IPv4 Address).*?:(.*?)\\r")
m=p.search(text)
print("The Ip address is -",m.group(1))