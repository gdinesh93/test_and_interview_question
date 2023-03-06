    """Write a Python function to calculate the factorial of a given number using recursion."""
    
    # def fact(n):
    #     if n==1:
    #         return 1
    #     else:
    #         return n*fact(n-1)
    #
    # print(fact(5))
    
    """Write a Python program to find the first non-repeated character in a given string."""
    
    # st="python is so cool"
    # ls=[]
    # ls1=[]
    # for i in st:
    #     count=0
    #     for j in st:
    #         if i==j:
    #             count+=1
    #     ls.append(i)
    #     ls1.append(count)
    # print(ls,ls1)
    # ind=ls1.index(1)
    # print("the first non repeated character is =",ls[ind])
    
    """Write a Python program to remove duplicate elements from a list, keeping the order of the elements intact."""
    # ls=[2,4,1,2,1,5,6,7,1,9]
    # ls1=[]
    # for i in ls:
    #     if i not in ls1:
    #         ls1.append(i)
    # print(ls1)
    """Write a Python function to check whether a given string is a palindrome or not."""
    # def palindrome(st):
    #     s=""
    #     for i in st:
    #         s=i+s
    #     if s==st:
    #         print("the given string is palindrome")
    #     else:
    #         print("not palindrome")
    # palindrome("madam")
    
    """Write a Python program to count the number of vowels in a given string."""
    
    # a="this has to be done now"
    # vow=["a","e","i","o","u"]
    #
    # count=0
    # for i in a:
    #     if i in vow:
    #         count+=1
    # print(count)
    """Write a Python program to find the second largest number in a given list."""
    # ls=[1,3,100,20,34]
    #
    # for i in range(len(ls)):
    #     for j in range(len(ls)):
    #         if ls[i]<ls[j]:
    #             ls[i],ls[j]=ls[j],ls[i]
    # print(ls[-2])
    
    """Write a Python program to check whether a given number is a perfect square or not."""
    
    # n=225
    # flag=True
    # for i in range(1,int(n/2)+1):
    #     if i*i==n:
    #         print("the number is perfect square =",i)
    #         flag=False
    # if flag:
    #     print("the number is not perfect square")
    
    """Write a Python program to find the sum of all the prime numbers between 1 and a given number."""
    # n=20
    # ls=[]
    # for i in range(2,n):
    #     for j in range(2,i):
    #         if i%j==0:
    #             break
    #     else:
    #         ls.append(i)
    #
    # print(sum(ls))
    
    """Write a Python program to generate all possible combinations of a given string."""
    # st="gone"
    # ls=[x for x in st]
    # n=len(st)
    # ls1=[]
    # def rand_gen(n):
    #     w=""
    #     flag=True
    #     while flag:
    #         c=random.choice(ls)
    #         if st.count(c)==w.count(c):
    #             pass
    #         else:
    #             w=w+c
    #         if len(w)==n:
    #             flag=False
    #     return w
    #
    # flag=True
    # while flag:
    #     s=rand_gen(n)
    #     if s not in ls1:
    #         ls1.append(s)
    #     if len(ls1)>=n*n:
    #         flag=False
    #
    # print(ls1)
    
    """Write a Python program to sort a given list of strings based on the length of each string."""
    # ls=["this", "is","the","python","program"]
    # ls1=[]
    # for i in ls:
    #     count=0
    #     for j in i:
    #         count+=1
    #     ls1.append(count)
    # print(ls1)
    # d=dict(zip(ls1,ls))
    #
    # ls1.sort()
    # ls2=[]
    # for i in ls1:
    #     ls2.append(d[i])
    # print(ls2)
    
    """Write a Python program to find the maximum sum of a subarray in a given list of integers."""
    
    """Write a Python program to implement the binary search algorithm to find the index of a given element in a sorted list of integers."""
    """Write a Python program to implement the merge sort algorithm to sort a given list of integers."""
    """Write a Python program to find the most frequent element in a given list of integers."""
    # ls=[2,4,6,3,2,4,6,7,2,5,7]
    #
    # d={}
    # for i in ls:
    #     if i not in d:
    #         d[i]=1
    #     else:
    #         d[i]+=1
    #
    # key=list(d.keys())
    # value=list(d.values())
    # ind=value.index(max(value))
    # print(key[ind])
    
    """Write a Python program to reverse the order of words in a given sentence."""
    st="this is the python program"
    # t=st.split()
    # ls=[]
    # for i in range(-1,-len(t)-1,-1):
    #     ls.append(t[i])
    # print(" ".join(ls))
    
    """Write a Python program to find the intersection of two given lists of integers."""
    # ls=[1,2,3,5,4,8]
    # ls1=[2,5,6,1,8,3]
    # ls2=[]
    #
    # for i in ls:
    #     if i in ls1:
    #         ls2.append(i)
    #
    # print(ls2)
    """Write a Python program to implement a stack data structure using a list."""
    """Write a Python program to implement a queue data structure using a list."""
    """Write a Python program to implement the depth-first search algorithm to traverse a given graph."""
    """Write a Python program to implement the breadth-first search algorithm to traverse a given graph."""
    
