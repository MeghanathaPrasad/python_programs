ss="abc5dddefggggda" 
res=""
s=0
while s<len(ss):
    if ss[s].isalpha():
        t=1
        while s+1<len(ss) and ss[s]==ss[s+1]:
            t+=1
            s+=1
            print(s)
        res+=ss[s]+str(t) 
    else:
        res+=ss[s]     
    s+=1
    
print(res)