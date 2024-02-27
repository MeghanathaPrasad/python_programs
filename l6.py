s=('1-3','4-4','5-8','10-15')
res=[]
for i in s:
    temp=i.split("-")
    for j in range(int(temp[0]),int(temp[-1])+1):
        res.append(j)

print(res)



# method-2

# s=('1-3','4-4','5-8','10-15')
# res=[]
# for i in s:
#     temp=i.split("-")
#     res+=(range(int(temp[0]),int(temp[-1])+1))
# print(res)


# method-3
# t='1-3,4-4,8-13'
# #[1,2,3,4,8,9,10,11,12,13]
# l=t.split(',')
# print(l)
# # print(list(range(1,3)))
# op=[]
# for i in l:
#     i=i.split('-')
#     x,y=int(i[0]),int(i[1])
#     # print(x,y)
#     op+=(range(x,y+1))
# print(op)