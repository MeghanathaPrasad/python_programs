
# grades=[75,67,38,33]
# temp=[45,50,55,60,65,70,75,80,95,100]
# for i in grades:
#     if i in temp:
#         print(i)

    
#     elif i+=i%10 in temp:
#         print(i)


# a=-10
# b=a<<2
# print(b)

# a=10
# b=5
# c=a|b

# print(c)

# l=[1,2,3,4,5]

# d={}
# for i in range(len(l)):
#     d[str(i)]=i+i

# print(d)

# l.append({'a':1,'b':2})
# print(l)
# d=l[5]
# print(d.values())
# dd={1:1,2:2}
# print(type(dd.keys()))
# for key, value in enumerate (d.values()):
#     print("Key: ", key ,"value: ",value)


# class A:
#     name ="icici"
#     def __init__(self,a,b):
#         self.a=a
#         self.b=b

#     def method_1(self):
#         print("running method 1 of the class A")

# class B(A):
#     def __init__(self,x,y,a,b):
#         super().__init__(a,b)
#         self.x=x
#         self.y=y

#     def method_2(self):
#         print("Running Method 2 of Class B")

# class C(B):

#     def __init__(self, x, y, a, b,n,m):
#         super().__init__(x, y, a, b)
#         self.N = n
#         self.M = m
    
#     def method_3(self):
#         return super().method_2()
    
    
# b=B(100,200,10,20)
# print(b.x)
# print(b.a)
# c=C(100,200,10,20,1,2)
# print(c.N)
# c.method_3()

# print(c.name)
# b.method_1()
# print(b.name)




# from abc import ABC, abstractmethod

# class myclass(ABC):
#     def common(self):
#         print('Running common method')

#     @abstractmethod
#     def method(self):
#         pass

# def do_something():
#     print('Doing something')


# if __name__ == '__main__':
#     do_something()

# print(dir())
# print(f"the __name__ is {__name__}")


# d={1:"one",2:"two",3:"three"}
# d[1]="One"
# print(d)
# # print(d.__dir__())
# l=[1,2,3,4]
# print(l.__dir__())

# for i,k in d.items():
#     print(i,k)


# def decorator_oldFun(fun):
#     def wrapper(*args,**kwargs):
#         print("Before calling the function")
#         fun(*args,**kwargs)

#     return wrapper

# @decorator_oldFun
# def old_fun():
#     print("this is old function")

# old_fun_dec = decorator_oldFun(old_fun)
# old_fun_dec()

# old_fun()


# def dec_div(fun):
#     def wrapper(a,b):
#         if a<b:
#             a,b=b,a
#         return fun(a,b)

#     return wrapper

# @dec_div
# def div(a,b):
#     return(a/b)

# print(div(10,5))


# l=[10,20,30,40,50]
# print(l.__dir__())
#[15,25,35,45,55]


# def func(n):
#     return n+5

# obj=(map(lambda n: n+5,l))
# print(list(obj))


# l=[45,75,65,95,25]

# d={1:{'a':10,'b':20},2:'two'}
# # print(d[1]["a"])
# for i in d.items():
#     print(i)
# del d[1]
# print(d)

# for i, v in d.items():
#     print(i,v)

# dd=dict(a=10,b=20,c=30)
# aa=dict(dd)
# print(aa)

# f=open("file.txt","w")
# f.write("HI good evening")
# print(f.readable())

# f.close()

# f=open("file.txt","r")
# print(f.readline(),end="")

# with open("file.txt","r") as f:
#     print(f.readlines())


# my_list = [1, 2, 3, 3,3, 4, 4,4,4,4, 5]
# res={}

# for i in my_list:
#     if i not in res:
#         res[i]=1
#     else:
#         res[i]=res[i]+1
# print(list(res.values()))
# print(res)

# for i in my_list:
#     if my_list.count(i)>1:
#         my_list.
# print(my_list)

# for i in my_list:
#     if i not in res:
#         res.append(i)
# print(res)


# my_dict = {'a': 3, 'b': 1, 'c': 2}
# sorted_dict = {k: v for k, v in sorted(my_dict.items(), key=lambda item: item[1])}
# print(sorted_dict)  # Output: {'b': 1, 'c': 2, 'a': 3}


# my_dict={'a':3,'b':7,'c':1,'d':0}

# # sorted(my_dict,)
# print((my_dict))

# sort_my_dict = {k:v for k,v in (sorted(my_dict.items(),key=lambda item : item[1],reverse=True))}

# print(sort_my_dict)


# try:
#     with open('myfile.txt', 'r') as file:
#         content = file.read()
# except FileNotFoundError:
#     print("File not found.")
# except PermissionError:
#     print("Permission denied.")
# except Exception as e:
#     print("An error occurred:", e)


# number= range(1,5)
# it = iter(number)
# print(next(it))
# print(next(it))
# print(next(it))


# import copy
# l=[1,2,[3,4],5]
# l2=copy.deepcopy(l)

# print(id(l[2]))
# print(id(l2[2]))


# s="sheela is a good girl and sheela is a bad girl"
# sl=s.split()
# d={}
# for i in sl:
#     if i not in d:
#         d[i]=0
#     d[i]=d[i]+1
# print(d)

# for i in sl:
#     d[i]=d.get(i,0)+1
# print(d)

# l=["meghu","ajin","vishal","ram"]
# n=[100,200,300,400]

# d={}
# for i in range(len(l)):
#     d[l[i]]=n[i]
# print(d)


# l=[1,2,3,4,5,6,7]
# print(l[0])
# print(l[-1])
# sum_natural=0
# for i in range(l[0],l[-1]+1):
#     sum_natural+=i

# print(sum_natural)
# print(sum(l))

# print(sum_natural-sum(l))
# n=l[-1]
# sum1=0
# total = n*(n+1)//2
# print(total)
# print(sum(l))

# l=[1,2,2,3,4,5,6,3,1]

# di={}
# for i in l:
#     if i not in di:
#         di[i]=0
#     di[i]=di[i]+1
# print(di)

# di ={x:x**2 for x in range(1,6)}
# print(di)\

# l=[10,200,50,30,70,90,65,90,200]
# s=set(l)
# print(sorted(list(s))[-2])

# def nth_max(l,nth_max):
#     s=set(l)
# def sec_max(l):
#     f_max=float("-inf")
#     s_max=float("-inf")

#     for i in l:
#         if i>f_max:
#             s_max=f_max
#             f_max=i

#         elif  i>s_max and i!=f_max:
#             s_max=i
    
#     return s_max

# print(sec_max(l))


# from abc import ABC,abstractmethod

# class one(ABC):
#     @abstractmethod
#     def sum_of_two(self):
#         pass
#     @abstractmethod
#     def  subtraction_of_two(a,b):
#         pass

    
# obb=one()
# print(obb.sum_of_two())

# d={'d':10,'b':5,'c':20,'a':15}
# print(sorted(d))

# sort_d=sorted(d.items(),key=lambda item:item[1])
# print(sort_d)

# s={i:i**2 for i in range(1,6)}

# print(s)
# print(type(s))

# for i in range(2):
#     for j in range(2):
#         print(i+j,end=" ")

# print()
# l=[ {i:j} for i in range(2) for j in range(2) ]
# print(l)
# l=[[1,10],[2,20],[3,30],[4,40],[5,50]]

# for i in range(1,6):
#     for j in range(10,60,10):
#         if j==i*10:
#             print(i,j)
        

# res=[[i,j] for i in range(1,6) for j in range(10,60,10) if j==i*10]
# print(res)

# n=
# for i in range(1,n+1):
# #     for j in range(n):
        

# def fibo(n):
#     t=0
#     t1=1 
#     for i in range(n):
#         print(t)
#         t,t1=t1,t+t1

# fibo(10)

# def prime(n):
#     flag=True
#     if n == 1:
#         print(n, "is not a prime number")
#     else:
#         for i in range(2,n):
#             if n%i==0:
#                 flag=False
#                 break

#     if flag:
#         return n
#     # else:
#     #     print(n,"is not a prime number")
    
# print(prime(11))

# l=[1,2,3,4,5,6,7,8,9,10]
# ss=list(map(lambda x:x if x%2==0 else  -x, l))
# print(ss)

# def prime_range(n):
#     primes = []
#     for i in range(2,n+1):
#         flag=True
#         for j in range(2,i):
#             if i % j == 0:
#                 flag=False
#                 break
#         if flag:
#             primes.append(i)
#     return primes
# print(prime_range(20))


# s="5419423"
# n="4"
# res=[]
# for i in range(len(s)):
#     if s[i]==n:
#         res.append(int(s[:i]+s[i+1:]))

# print(res)

# s=(1,2,3,4,3)
# print(s.index(4))

# n=123
# rev=0
# while n>0:
#     rem=n%10
#     rev=rem+rev*10
#     print(rev)
#     n//=10
# print(rev)

# print(1%10)

# n=5
# res=1
# for i in range(1,6):
#     res*=i
# print(res)


# n = 10
# fact = 1
 
# for i in range(1, n+1):
#     fact = fact * i
 
# print("The factorial of 23 is : ", end="")
# print(fact)

# my_dict = {'a': 3, 'b': 1, 'c': 2}
# sorted_dict = {k: v for k, v in sorted(my_dict.items(), key=lambda item: item[1])}
# print(sorted_dict)  # Output: {'b': 1, 'c': 2, 'a': 3}

# my_dict = {'c': 3, 'b': 1, 'a': 2}
# ll={k:v for k,v in sorted(my_dict.items(), key=lambda item:item[1])}
# # sorted_d={k:v for k,v in sorted(my_dict.items(), key=lambda item:item[1])}

# print(ll)
# sorted(my_dict)
# print(my_dict)

# import copy
# l=[1,[2,3],4,5]
# l2=copy.deepcopy(l)
# # l2=l
# l2[2]=10000
# l2[1][0]=2000
# print(id(l))
# print(id(l2))


# print(l)
# print(l2)

# l=[1,2,3,4,5,6,7,8,9,10]
# print(10*(10+1)//2)
# print(sum(l))


# res = [(i,j) for i in range(1,6) for j in range(10,60,10) if j==i*10]

# print(res)

#generator

# def generat_fib():
#     a,b=0,1
#     while True:
#         yield a
#         a,b=b,a+b




# gen=generat_fib()
# print(dir(gen))
# for i in range(10):
#     print(next(gen))

# l=[2,3,4,5,8,7]
# r=2
# # r=r%len(l)
# res=l[-r:]+l[:-r]

# print(res)
class a:
    @staticmethod
    def Even(a):
        return a<2
print(a.Even(1))