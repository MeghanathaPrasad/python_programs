
# def sum_of_num(a,b,sums=0):
#     if a<=b:
#         sums+=a
#         return sum_of_num(a+1,b,sums)
#     return sums
# x=sum_of_num(4,11)
# print(x)

#what is recursion 
# Ans: A function calling itself i called recursion . It is the process in which a function calls itself during its execution. This self-invoking

import sys

# print(sys.getrecursionlimit())  #default value is 1000

# sys.setrecursionlimit(2000)

# print(sys.getrecursionlimit())


# def greet():
#     print("Hello")
#     greet()

# greet()

# finding factorial
#___________________

# def fact(n):
#     if n == 0:
#         return 1
#     return n * fact(n-1)

# print(fact(5))






#Finding substring  in string  in recursion

# def issubstring(str1,str2):
#     size1= len(str1)
#     size2= len(str2)
#     if size1 == 0:
#         return False
#     if size2 == 0:
#         return True
#     if str1[0]==str2[0]:
#         return exactsame(str1,str2)
#     return issubstring(str1[1:],str2)

# def exactsame(str1,str2):
#     size1= len(str1)
#     size2= len(str2)
#     if size1 == 0:
#         return False
#     if size2 == 0:
#         return True
#     if str1[0]==str2[0]:
#         return exactsame(str1[1:],str2[1:])
#     return  False

# s1="meghanath"
# s2="es"
# print(issubstring(s1,s2))



#reversing the list using recursion

# def reverse1(str):
#     size = len(str)
#     if size == 0:
#         return
#     last_chr=str[size-1]
#     print(last_chr,end=" ")
#     reverse1(str[0:size-1])

# reverse1("meghanath")

# n=10
# def fibo(n)

# a=0
# b=1
# for i in range(10):
#     print(a)
#     a,b=b,a+b
# n=10
# def fibo(n,a=0,b=1):
#     if n>0:
#         print(a)
#         a,b=b,a+b
#         fibo(n-1,a,b)

# fibo(n)


# n=int(input("Enter the number: "))
# res=1
# for i in range(1,n+1):
#     res*=i
# print(res)


n=5
def fact(n,res=1):
    if n>0:
        res*=n
        return fact(n-1,res)
    
    return res
print(fact(n))

def fact(n):
    if n==1 or n==0:
        return 1
    return n*fact(n-1)
print(fact(5))





