def supr_div(func):
    def inner(a,b):
        if a<b:
            a,b=b,a
        return func(a,b)
    return inner


@supr_div
def div(a,b):
    return a/b

# print(div(10,5))


# div=supr_div(div)
# print(div(5,10))

# import copy

# l=[1000,20,30,[1,2]]
# m=copy.deepcopy(l)
# n=l.copy()

# l[0]=0

# print(m,n)


l = lambda a:a*2
print(l(2))



