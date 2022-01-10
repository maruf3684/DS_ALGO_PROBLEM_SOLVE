arr=[9,7,6,5,4,3,1,1,56,3,3,22,111]


def marge(left,right):
    i=0
    j=0
    arr2=[]
    k=0
    while((i<left.__len__()) and (j<right.__len__())):
        if left[i]<right[j]:
            arr2.insert(k,left[i])
            k+=1
            i+=1
        else:
            arr2.insert(k,right[j])
            k+=1
            j+=1
 
     

    while(i<left.__len__()):
            arr2.insert(k,left[i])
            k+=1
            i+=1
          
          
    while(j<right.__len__()):
            arr2.insert(k,right[j])
            k+=1
            j+=1
           
    return arr2


def margesort(arrays):
    if arrays.__len__()==1: 
        return arrays;
    mid=(arrays.__len__()-1)//2
    left=margesort(arrays[0:mid+1])
    right=margesort(arrays[mid+1:arr.__len__()])
    return marge(left,right)

print(margesort(arr))




