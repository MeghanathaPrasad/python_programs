

# print(add)
def decr_add(func):
    def wrapper(a,b):
        if a < b:
            a,b=b,a
        return func(a,b)
    return wrapper
@decr_add
def div(a,b):
    return a/b

# div=decr_add(div)
# print(div(5,10))
print(div(5,10))