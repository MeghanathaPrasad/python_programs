# s="1231"
# s1="1"
# op=231
s="65661"
s1="6"
# op="6561"

res=[]
for i in range(len(s)):
    if s[i]==s1:
        res.append(s[0:i]+s[i+1:])
print(res)
print(max(res))