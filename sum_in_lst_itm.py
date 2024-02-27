l= [123,456,789]
r = []
for i in l:
    t = 0
    for j in str(i):
        t=t+int(j)
    r.append(t)
    t=0

print(r)



# l= [123,456,789]
# ans=[]
# for i in l:
#     t=i
#     sum=0
#     while t!=0:
#         print(t)
#         r=t%10
#         t=t//10
#         sum+=r
#     ans.append(sum)
# print(ans)






















