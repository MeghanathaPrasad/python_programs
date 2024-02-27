x11=4523
v11=8092
x22=9419 
v22=8076


def kangaroo(x1, v1, x2, v2):
    # Write your code here
    
    while (x1 != x2) and (x2<=10000*v2 and x1<=10000*v1):
        x1+=v1
        x2+=v2
    
    if x1 == x2:
        return "YES"
    else:
        return "NO"
    
print(kangaroo(x11,v11,x22,v22))