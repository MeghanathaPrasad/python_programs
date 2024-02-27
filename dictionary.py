keys = ['a','b','c','d','e']
values = [1,2,3,4,5]  

# dict = {k:v for (k,v) in zip(keys,values)}

# print(dict) #{'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}


# dic={}
# for i in range(len(keys)):
#     dic[keys[i]]=values[i]
# print(dic)


# dic=dict.fromkeys(range(5),15)
# print(dic)\
#o/p:  {0: 15, 1: 15, 2: 15, 3: 15, 4: 15}



# sDict = {x.upper(): x*3 for x in 'coding '}
# print (sDict)
#o/p: {'C': 'ccc', 'O': 'ooo', 'D': 'ddd', 'I': 'iii', 'N': 'nnn', 'G': 'ggg', ' ': '   '}


#nested dict comprehension

# given string
l="GFG"
 
# using dictionary comprehension
dic = { x: {y: x + y for y in l} for x in l}
 
print(dic)