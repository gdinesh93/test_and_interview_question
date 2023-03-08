"""1.print a multiplication table."""
import copy


def multiplication(n):
    for i in range(1, 11):
        print("{} X {} = {}".format(i, n, i * n))


multiplication(7)

"""2.for a given input print the value from a given dictionary"""

d = {1: "apple", 2: "orange", 3: "pear", 4: "grapes"}

n = int(input("enter the key from {} to have the value-".format(list(d.keys()))))

print("The value of {} is {}".format(n, d[n]))

"""Write a program to find the elements of a list that have least difference in python? 
input = [3,9,50,15,99,7,98,65] output = [98,99]
"""
ls = [3, 9, 50, 15, 99, 7, 98, 65]
ls.sort()
mini = ls[1] - ls[0]
for i in range(len(ls)):
    for j in range(i + 1, len(ls)):
        if ls[j] - ls[i] < mini:
            mini = ls[j] - ls[i]
for i in range(len(ls)):
    for j in range(i + 1, len(ls)):
        if ls[j] - ls[i] == mini:
            print([ls[j], ls[i]])

"""Get the lines above and below of the line containing a string."""
with open(
    r"C:\Users\HP\PycharmProjects\selenium\pytestDemo\python question.txt",
    "r",
    encoding="utf-8",
) as f:
    p = f.readlines()

st = "containing"

for i in p:
    if st in p:
        continue
    else:
        print(i)

"""5.Write a Python program to produce half pyramid using *."""

n = 5
for i in range(n):
    for j in range(i + 1):
        print("*", end="")
    print()

"""6.Print a list of odd index elements from list1 and even index elements from list2 and print the thrid list with the result set of both. 
list1 = [3,6,9,12,15,18,21] list2 = [4,8,12,16,20,24,28]
"""
list1 = [3, 6, 9, 12, 15, 18, 21]
list2 = [4, 8, 12, 16, 20, 24, 28]
ls_odd = []
ls_even = []
count = 1
for i in list1:
    if count % 2 != 0:
        ls_odd.append(i)
    count += 1

count = 0
for i in list2:
    if count % 2 == 0:
        ls_even.append(i)
    count += 1
print(ls_odd)
print(ls_even)
ls_even.extend(ls_odd)
print(ls_even)

"""
7.write a python program to print the repititve characters in a list which should exclude integers 
input = ['a','a',4,4,'b','c','a'] output = {'a':3} 
"""
ls = ["a", "a", 4, 4, "b", "c", "a"]
d = {}
for i in ls:
    if type(i) is str:
        if i not in d:
            d[i] = 1
        else:
            d[i] += 1
print(d)
key = list(d.keys())
val = list(d.values())
ind = val.index(max(val))
d1 = copy.deepcopy(d)
for i in d1:
    if i != key[ind]:
        d.popitem()
print(d)

"""8.write a program to count the no.of characters in a string. 
input : "I am good at python" output : {'g':1, '0:3, 'a':2, ...}
"""
st = "I am good at python"
d = {}
for i in st:
    if i != " ":
        if i not in d:
            d[i] = 1
        else:
            d[i] += 1
print(d)


"""9.write a program to find missing numbers from a list
"""

ls = [1, 3, 5, 7, 8, 9]
mini = min(ls)
maxi = max(ls)
ls1 = []
for i in range(mini, maxi + 1):
    if i not in ls:
        ls1.append(i)
print("the missing numbers are-", ls1)

"""10.create a fibonacci series of 100 using recursive function
"""


def fib(n):
    if n == 0 or n == 1:
        return n
    else:
        return fib(n - 1) + fib(n - 2)


count = 0
while True:
    print(fib(count))
    count += 1
    if fib(count) > 100:
        break

"""11.write a program to check if a given positive integer is a power of two
"""
n = int(input("enter the number"))

if n < 1:
    print("negative number provided, retry")
else:
    if n == 1:
        print("the number is power of 2")
    if n % 2 != 0 and n != 1:
        print("The number {} is not the power of 2")
    if n % 2 == 0:
        while True:
            n = n / 2
            if n <= 1:
                break
        print(n)
        if n == 1:
            print("the number is power of 2")

        else:
            print("the number is not the power of 2")

"""12.write a list comprehension to print a list from 1 to 10
"""

ls = [x for x in range(1, 11)]
print(ls)

"""13.How to remove the nth occurrence of the word from a list?
"""

ls = ["This", "is", "the", "word", "that", "has", "the", "power"]
ls2 = []
n = 2
w = "the"
count = 0
for i in ls:
    if i == w:
        count += 1
        if count < n:
            ls2.append(i)
        elif count == n:
            continue
    else:
        ls2.append(i)
print(ls2)

"""14.Print HELLO for the given string “AHCECLWLXO”.
"""
st = "AHCECLWLXO"
st1 = ""
count = 0
for i in st:
    count += 1
    if count % 2 == 0:
        st1 = st1 + i
print(st1)

"""15.Print HELLO in CAPITAL letters for the given string “ahceclwlxo”.
"""
st = "ahceclwlxo"
st2 = ""
count = 0
for i in st:
    count += 1
    if count % 2 == 0:
        st2 = st2 + i.upper()
print(st2)

"""16.Ask the user to enter a number and then print the multiplication table of that number
"""


def multi(n):
    for i in range(1, 11):
        print("{} X {} = {}".format(i, n, i * n))


num = int(input("enter the number for multiplication"))
multi(num)

"""17.Ask the user to enter two number (int) a and b, return true if a) either one is 6 
b) or if their sum is 6 c) or the difference is 6
"""


def check(list1):
    list1.sort()
    if (
        list1[1] - list1[0] == 6
        or list1[0] == 6
        or list1[1] == 6
        or list1[0] + list1[1] == 6
    ):
        return True
    else:
        return False


ls = []
for i in range(2):
    n = int(input("enter the number"))
    ls.append(n)
print(check(ls))

"""18.Ask the user to input a string of odd length, return the string length 3 from its middle. 
The string length will be at least 3.
"""
st1 = input("enter the string")
if len(st1) >= 3:
    if len(st1) % 2 == 0:
        print("enter the string with odd value")
    else:
        mid = len(st1) // 2
        print(st1[mid : mid + 3])

"""19.Given 2 strings, a and b, return a new string made of the first char of a and the last char of b. 
If either string is length 0, use ‘@’ for its missing char.
"""
a = input("enter a string")
b = input("enter another string")
if len(a) == 0:
    c = "@" + b[-1]

if len(b) == 0:
    c = a[0] + "@"
if len(a) == 0 and len(b) == 0:
    c = "@" + "@"
else:
    c = a[0] + b[-1]

print(c)

"""20.Given a string, return true if “bad” appears starting at index 0 or 1 in the string, 
The string may be any length, including 0.
"""

n = "ebad"


def bad_check(n):
    if n[:3] == "bad" or n[1:4] == "bad":
        return True


print(bad_check(n))

"""21.Ask user to input a string, return a new string where for every char in the original, there are two chars.
Ex1: (“The”) → “TThhee”
Ex2: (“AAbb”) → “AAAAbbbb”
Ex3: (“Hi-There”) → “HHii–TThheerree”"""

n = input("enter the string")

s = ""
for i in n:
    s = s + i + i
print(s)

"""22.Given an array length 1 or more of ints, return the difference between the largest and smallest values 
in the array.
"""

ls = [2, 6, 10, 14, 16]
ls.sort()
print("the difference is =", ls[-1] - ls[0])

"""23. Given an array of ints, return true if the number of 1’s is greater than the number of 4’s
"""


def num_check(ls):
    count1 = 0
    count4 = 0
    for i in ls:
        if i == 1:
            count1 += 1
        if i == 4:
            count4 += 1
    if count1 > count4:
        return True
    else:
        return False


ls1 = [1, 3, 1, 1, 4, 1, 4, 1, 1, 4, 4, 1, 4, 1, 4, 1, 4, 1, 4, 4, 4, 4, 4, 4, 4]
print(num_check(ls1))

"""24.write a program to swap 2 numbers without out 3rd variable
"""

a = 10
b = 15
a, b = b, a
print(a)
print(b)

"""25.write a program to print occurance if character using dictionary comphersion
"""

st1 = "thishastobe"
d = {char: st1.count(char) for char in st1}
print(d)

"""26.Write pgm to find prime numbers using list comprehension
"""

n = 22
count = 0
for i in range(1, n + 1):
    if n % i == 0:
        count += 1
if count == 2:
    print("the number is prime")
else:
    print("the number is not prime")


for i in range(2, 50):
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        print(i)


"""27.Write a Program to print sum of even numbers which is divisible by 8:-
"""

even = [x for x in range(100) if x % 2 == 0]

print(even)
ls = []
for i in range(len(even)):
    for j in range(i + 1, len(even)):
        if (even[i] + even[j]) % 8 == 0:
            ls.append(([even[i], even[j]]))

print(ls)

"""28.Write a function to return the nth fibonacci number. The first two can be assumed to be 1 and 1. 
The third and fourth are then calculated to be 2 and 3.
"""


def fib_num(n):
    a = 0
    b = 1
    fib = []
    fib.append(a)
    for i in range(100):
        fib.append(b)
        sum = a + b
        a = b
        b = sum
    print("{}th/rd/st fibonacci number is {}".format(n, fib[n]))


fib_num(4)

"""29.[4,5,6,7,2,3,11,13] Sort the element in a such a way that have even should come first and odd numbers at last.
"""

ls = [4, 5, 6, 7, 2, 3, 11, 13]
even = [x for x in ls if x % 2 == 0]
odd = [x for x in ls if x % 2 != 0]
even.sort()
odd.sort()
even.extend(odd)
print(even)

"""30.Print odd numbers as it is and double the even numbers.
"""
ls = []
for i in range(50):
    if i % 2 != 0:
        ls.append(i)
    else:
        ls.append(i * 2)
print(ls)

"""31.the sum of 100 numbers divisible by 2 but not 8
"""

ls = [x for x in range(1, 101)]
ls1 = []
for i in range(len(ls)):
    for j in range(i + 1, len(ls)):
        if (ls[i] + ls[j]) % 2 == 0 and (ls[i] + ls[j]) % 8 != 0:
            ls1.append([ls[i], ls[j]])
print(ls1)

"""32. Write a code for Capitalize ( Refer the in put and output ) sample input : getCodeType output: Code_Type i/p : getCodeStyle o/p: Code_Style i/p: getSWIFTCode o/p: SWIFT_Code
"""

st = "getCodeStyle"
w = ""
count = 0
for i in st:
    if i.isupper():
        count += 1
    if count == 1:
        w = w + i
    if count > 1 and w[-1].islower() and i.isupper():
        w = w + "_"
    if count > 1:
        w = w + i
print(w)

"""33.if a number divide in 3 print "hello", in "5" print "world", in 15 print "helloworld"
"""

for i in range(1, 16):
    if i % 3 == 0 and i % 5 == 0:
        print("hello world")
    elif i % 3 == 0:
        print("hello")
    elif i % 5 == 0:
        print("world")

    else:
        print(i)

"""34.find even number betweens 1 to 100 and not divisible by 8 
"""

ls = [x for x in range(1, 101) if x % 2 == 0 and x % 8 != 0]
print(ls)

"""35.Create a dictionary like this : {a:1, b:2, c:3, d:4, e:5}
"""


d = {}
char = 97
for i in range(1, 6):
    d[chr(char)] = i
    char += 1
print(d)


"""36.my_list = [[35, 66, 31], ["python", 13, "is"], [15, "fun", 14]] OUTPUT REQUIRED: 
To print the string from the list as : python is fun
"""
my_list = [[35, 66, 31], ["python", 13, "is"], [15, "fun", 14]]
ls = []
for i in range(len(my_list)):
    if type(my_list[i]) is list:
        for j in my_list[i]:
            try:
                if j.isalpha():
                    ls.append(j)
            except:
                pass

print(" ".join(ls))

"""37.Write a function that takes an array of integers and returns that array rotated by N positions 
using Python or Ruby or JavaScript. For example, if N=2, given the input 
array [1, 2, 3, 4, 5, 6] the function should return [5, 6, 1, 2, 3, 4]
"""
ls = [1, 2, 3, 4, 5, 6]
n = 2
print(ls[len(ls) - 2 :] + ls[: len(ls) - 2])

"""38.find minimum number in list without using comparison operator. 
"""
ls = [3, 4, 9, 2, 6, 1, 5]

ls1 = copy.deepcopy(ls)

while True:
    n = 1
    flag = False
    for i in range(len(ls1)):
        ls1[i] = ls1[i] - n
        if ls1[i]:
            pass
        else:
            flag = True
            break
    if flag:
        break


ind = ls1.index(0)
print("the minimum number is=", ls[ind])

"""find the second largest number for the lst=[1, 99, 100, 103, 103]"""

ls = [1, 99, 100, 103, 103]
maxi = max(ls)
min_dif = maxi - ls[0]
for i in range(len(ls)):
    if maxi - ls[i] < min_dif and maxi - ls[i] != 0:
        min_diff = maxi - ls[i]

print(min_diff)
print("the second largest number is-", maxi - min_diff)
"""40. Check if "(()))(" is a valid pair of parenthesis or not."""

st1 = "(())()()"
ls = []
for i in st1:
    if i == "(":
        ls.append(i)
    elif i == ")":
        try:
            ls.pop()
        except:
            pass
if ls:
    print("not valid")
else:
    print("valid")
