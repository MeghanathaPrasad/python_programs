l=[2,3,1,4,6,5,9,7]

def merg_sort(l):
    if len(l)>1:
        left_arr=l[:len(l)//2]
        right_arr=l[len(l)//2:]

        #recursion
        merg_sort(left_arr)
        merg_sort(right_arr)

        #merge
        i=0 #left_arr_indx
        j=0 #right_arr_indx
        k=0 #merged_arr_indx

        while i<len(left_arr) and j<len(right_arr):
            if left_arr[i]<right_arr[j]:
                l[k]=left_arr[i]
                i+=1
            else:
                l[k]=right_arr[j]
                j+=1
            k+=1

        while i<len(left_arr):
            l[k]=left_arr[i]
            i+=1
            k+=1
        
        while j<len(right_arr):
            l[k]=right_arr[j]
            j+=1
            k+=1

print(l)
merg_sort(l)
print(l)