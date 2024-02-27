s="^&^&^&H()oW90 a#$Re y&*78o””U"
# op='how are you'

# r=""
# for i in s:
#     if i.isalpha() == True or i ==" ":
#         r+=i.casefold()
# print(r)

# r=""
# for i in s:
#     t=ord(i)
#     print(t)
#     if (t>=97 and t<=122) or i==' ':
#         print('i-->',i)
#         r+=i
#     elif t>=65 and t<=90:
#         r+=chr(t+32)

# print(r)   
# print(ord('~'))
        

# print(r)
# # 65-90 97-122
# print())

# import re
# s="^&^&^&H()oW90 #$Re y&*78o””U"
# match=re.sub(r'[^a-zA-Z\s]','',s)
# print(match)



a = int(input("enter first number: "))
b= int(input("enter the sencond number: "))

min = min(a,b)
max = max(a,b)
r=0
# for i in range(min,max):
#     r+=i

# print(r)

res = [i for i in range(min,max)]
print(sum(res))