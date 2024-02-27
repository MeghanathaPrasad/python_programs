# L=[2,3,1,4,5,0,10,5,1,100,50,100]
# li=set(L)
# l=list(li)


# print(l)
# for i in range(len(l)):
#     cur_min = i
#     for j in range(i+1,len(l)):
#         if l[j]<l[cur_min]:
#             cur_min=j

#     l[i],l[cur_min]=l[cur_min],l[i]

# print(l)

l=[3,4,2,1,6,3,6,2,0,8]
print(l)
for i in range(len(l)):
    cur_min=i
    for j in range(i+1,len(l)):
        if l[j]<l[cur_min]:
            cur_min = j
    l[i],l[cur_min]=l[cur_min],l[i]

print(l)