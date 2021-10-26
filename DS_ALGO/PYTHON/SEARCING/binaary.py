
arr=[1,2,4,5,6,7,89,99,555]
arr2=[99,78,66,55,55,46,44,43,3]


def binaryMal(arr,terget):
    isAcc=False
    if arr[0]<arr[len(arr)-1]:
        isAcc=True
        
    start=0
    end=len(arr)-1

    while(start<end):
        mid=(start+end)//2
        if isAcc:
            if(terget>arr[mid]):
                start=mid+1
            elif(terget<arr[mid]):
                end=mid-1
            elif(terget==arr[mid]):
                return mid
        else:
            if(terget<arr[mid]):
                start=mid+1
            elif(terget>arr[mid]):
                end=mid-1
            elif(terget==arr[mid]):
                return mid

    return -1


print (binaryMal(arr,6))


