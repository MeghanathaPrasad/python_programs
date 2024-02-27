# def insertion_sort(A):
#     for i in range(1, len(A)):
#         curNum=A[i]
#         for j in range(i-1,0,-1):
#             if A[j]>curNum:
#                 A[j+1]=A[j]
#             else:
#                 A[j+i]=curNum
#                 break
# A=[3,4,1,2,5]

# insertion_sort(A)
# print("Sorted array is",A)


#bubbel sort

# l=[3,2,1,5,6,0,2,1,7]
# print(l)
# for i in range(len(l)-1,0,-1):
#     for j in range(i):
#         if l[j]>l[j+1]:
#             l[j],l[j+1]=l[j+1],l[j]

# print(l)

l=[1,2,3]
l2=[5,6,7]
z=(zip(l,l2))
print(list(z))