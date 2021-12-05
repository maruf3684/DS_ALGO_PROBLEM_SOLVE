arr=[4,6,2,5,7,9,1,3]
#arr=[3,2]
arr=[2,3]

def partition(arr,high,low):
    pivot=low
    i=low
    j=high
    
    while(i<j):
        while((arr[i]<=arr[pivot])and(i<j)):
            i=i+1


        while((arr[j]>arr[pivot])):
            j=j-1

        if(i<j):
            arr[i], arr[j] = arr[j], arr[i]

    arr[pivot], arr[j] = arr[j], arr[pivot]
    return j


def quicksort(arr,high,low):
    if low<high:
        j=partition(arr,high,low)
        quicksort(arr,j-1,low)
        quicksort(arr,high,j+1)


quicksort(arr,len(arr)-1,0)

print(arr)
        


    

