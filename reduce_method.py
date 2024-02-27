# from functools import reduce
# # def ad(a,b):
# #     return a-b
l=['1','2','3','4','5']
# # print(type(l[0]))
# # res = reduce(lambda a,b: a+b,l,'10000')
# # print(res)

# def f(a,b):


def reducee(func,iterables,default=0):
    if type(iterables[0]) == str:
        res=iterables[0]
    elif type(iterables[0]==int):
        res = iterables[0]

    for i in range(len(iterables)-1):
        try:
            res = func(res,iterables[i+1])
        except:
            pass
        
    return default+res

ress=reducee(lambda a,b:a-b,l,'100')
print(ress)

# l=['1','2','3','4','5','7']
# def add(a,b):
#     return a+b
# def re(func,iter,initial=0):
#     if (initial==0):
#         res=iter[0]
#     else:
#         res=func(initial,iter[0])
#     for i in range(len(iter)-1):
#         # if(i==len(iter)-2):
#         #     return res+=iter[len(iter)-1]
#         # else:
#         res=func(res,iter[i+1])
#         # print(func(iter[i],iter[i+1]))
#     return(res)
# ans=re(add,l,'10')
# print(ans)
