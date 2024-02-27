# write code to extract integer from string and return the sum of all integers
s = 'ms1875yste21chnono19gis101'
# output = 2016

def count_num_str(s):
    res=0
    tem=""
    for i in range(len(s)):
        if s[i] in "1234567890":
            tem+=s[i]
        else:
            tem+=" "
    aa=tem.split(" ")
    for i in aa:
        if i:
            res+=int(i)
    return res

res=count_num_str(s)
print(res)