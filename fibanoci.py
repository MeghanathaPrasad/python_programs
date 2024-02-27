
def fibonoci(Range):
    a=0
    b=1
    for i in range(Range+1):
        yield a
        a,b=b,a+b
        

# x=fibonoci(10)
# print(next(x))
# print(next(x))
# print(next(x))

for i in fibonoci(10):
    print(i)


