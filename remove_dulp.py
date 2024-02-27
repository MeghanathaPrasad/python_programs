
#removing duplicates
# l=[1,2,1,3,4,4,5,6,2,3,9,10,10]
# res=[]
# for i in l:
#     if i not in res:
#         res.append(i)
# print(res)


# for i in l:
#     if l.count(i)>1:
#         l.remove(i)
# print(l)

# d={}
# for i in l:
#     d[i]=1
# print(list(d.keys()))


#reverse list

# l=[1,2,3,4,5,6,7]
# res=[]
# for i in range(len(l)-1,-1,-1):
#     res.append(l[i])
# print(res)

# s=0
# e=len(l)-1
# while s<e:
#     l[s],l[e]=l[e],l[s]
#     e-=1
#     s+=1
# print(l)

#rotation of list

l=[1,2,3,4,5]
r=12
r=r%len(l)
print(r)
# for i in range(r):
#     t=l[-1]
#     l.insert(0,t)
#     l.pop()
# print(l)

#right shift
# res=l[-r:]+l[:-r]
# print(res)

#left shift
# res=l[r:]+l[:r]
# print(res)

# #decorators

# def func1():
#     print("i am func1")



#sendond minium sencodn maximun
l=[1,-2,-3,10,100,9,-200,200,100,-3,100,-3,200,-200]
# set_list= set(l)
# print(set_list)
# sort_list = list(set_list)
# sort_list.sort()
# print(sort_list)
# print(sort_list[1])
# print(sort_list[-2])


# smin=-3
# smax=100

# def secdmin_secmax(l):
#     set_list= set(l)
#     sort_list = list(set_list)
#     sort_list.sort()
#     return sort_list[1],sort_list[-2]

# print(secdmin_secmax(l))


#methond 2 
# f_min = float("inf")
# s_min = float("inf")

# for i in l:
#     if i <f_min:
#         t = f_min
#         f_min = i
#         s_min = t
#     elif i != f_min and i<s_min:
#         s_min = i
# print(f_min, s_min)


#max
#  
# for i in range(l):
#     print(i)

s="abbcdeffgh"
# ss={}
# for i in s:
#     ss[i]=s.count(i)

# print(ss)

# ss=""
# for i in s:
#     if i not in ss:
#         ss+=i+"->"+str(s.count(i))
# print(ss)

# l=['9','11111','2','5','3','411']
# l=[5,11111,0,4,9,3,411]

# print(l)
# for i in range(len(l)):
#     for j in range(len(l)):
#         if int(l[i])<int(l[j]):
#             l[i],l[j]=l[j],l[i]

# print(l)


        



