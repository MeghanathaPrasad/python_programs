l=[3,2,9,1,4]
# print(l)
# for i in range(1,len(l)):
#     for j in range(i-1,0,-1):
#         if l[j]>l[j+1]:
#             l[j],l[j+1]=l[j+1],l[j]
#         else:
#             break
# print(l)

# def insertin_sort(A):
#     for i in range(1,len(A)):
#         j=i
#         while A[j-1]>A[j] and j>0:
#             A[j-1],A[j]=A[j],A[j-1]
#             j-=1


# print(l)
# insertin_sort(l)
# print(l)


l=[3,4,1,6,5]
print(l)
for i in range(1,len(l)):
    j=i
    while l[j-1]>l[j] and j>0:
        l[j-1],l[j]=l[j],l[j-1]
        j-=1
    
print(l)