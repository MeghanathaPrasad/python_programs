# fruits = {"apple":
#               {"qty": 200, "pkg_type": "unit", "price_per_pack": 20},
#           "orange":
#               {"qty": 300, "pkg_type": "pair", "price_per_pack": 30},
#           "banana":
#               {"qty": 600, "pkg_type": "dozen", "price_per_pack": 50}
#           }


# total_cost=0
# temp=[]
# for i in fruits.values():
#     temp.append(list(i.values()))

# print(temp)
# apple_cost=0
# orange_cost=0
# banana_cost=0
# for i in temp:
#     if i[1]=="unit":
#         total_cost+=i[0]*i[2]
#     elif i[1]=="pair":
#         total_cost+=(i[0]/2)*i[2]
#     elif i[1]=="dozen":
#         total_cost+=(i[0]/12)*i[2]

# print(total_cost)


# n=int(input"")

# l=[1,2,3,4,4,6,6,7,7] #second max

# fmax=float("-inf")
# smax=float("-inf")

# for i in l:
#     if l[i]>fmax:
#         smax=fmax
#         fmax=i
#     elif i<smax and i!=fmax:
#         smax=i

# print(fmax)
# print(smax)


# #Happy numer of the give number
n=12345

while n>=10:
    res = 0
    while n>0:
        res+=n%10
        n//=10
    n=res
print(res)




# print(tem)
# if tem>9:
#     while tem>0:
#         res+=tem%10
#         tem//=10
#     print(res)
# else:
#     print(tem)




# if tem>9:
#     while tem>0:
#         res+=tem%10
#         tem//=10


# # print(tem)
# # print(res)



# n = 1234

# # Continue the loop until n becomes a single-digit number
# while n >= 10:
#     temp = 0
    
#     # Calculate the sum of digits of n
#     while n > 0:
#         temp += n % 10
#         n //= 10
        
#     # Update n with the sum of its digits
#     n = temp

# # Print the final single-digit sum
# print(n)

# l=[1,2,3,4,4,6,6,7,7,0,5,2,8,6] #second max
# l2=[]
# print(l)
# for i in l:
#     if i not in l2:
#         l2+=[i]

# print("uniqe values in the list : ",l2)
# for i in range(len(l2)):
#     for j in range(i+1,len(l2)):
#         if l2[i]>l2[j]:
#             l2[i],l2[j]=l2[j],l2[i]
# print("sorted the uniqe list: ",l2)
# user_inp = int(input("Enter the Nth number to find the any maximun in the given list: "))
# print(f"the {user_inp}nd maximun in the give list is: ",l2[-user_inp])