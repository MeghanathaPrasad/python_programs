import copy 
# l=[1,2,3,4,5]
# l1=copy.copy(l)
# l2=copy.deepcopy(l)

# l1[0]=10
# l2[0]=100

# print(l,l1)
# print(l,l2)

# o/p
# [1, 2, 3, 4, 5] [10, 2, 3, 4, 5]
# [1, 2, 3, 4, 5] [100, 2, 3, 4, 5]





l=[1,2,3,[4,5],6]
l1=copy.copy(l)
l2=copy.deepcopy(l)

l1[3][0]=10
l2[3][0]=100

print(l,l1)
print(l,l2)

# o/p
# [1, 2, 3, [10, 5], 6] [1, 2, 3, [10, 5], 6]
# [1, 2, 3, [10, 5], 6] [1, 2, 3, [100, 5], 6]