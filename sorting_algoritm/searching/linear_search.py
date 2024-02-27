l=[1,2,3,4,4,5,6,7,8,9]
n=4
for i in range(len(l)):
    if l[i] == n:
        print(f"Found {n} at the index of {i}")
        break