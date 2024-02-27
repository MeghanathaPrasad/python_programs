l=[-1,5,3,9,2,10,-5]

for i in range(len(l)):
    for j in range(len(l)):
        if l[i] < l[j]:
            l[i],l[j]=l[j],[i]

print(l)