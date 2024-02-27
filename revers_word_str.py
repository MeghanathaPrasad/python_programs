# Input: s = "the sky is blue"
# Output: "blue is sky the"

s = "the sky is blue"
sl=s.split()
res=[]
print(sl)
for i in range(len(sl)-1,-1,-1):
    res.append(sl[i])
print(res)
r=' '.join(res)
print(r)