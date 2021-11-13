


def search(arr,start,end,terget):
    mid=(start+end)//2

    if start>end:
        return -1

    if(terget==arr[mid]):
        return mid

    elif(terget>arr[mid]):
        return search(arr,mid+1,end,terget)

    elif(terget<arr[mid]):
        return search(arr,start,mid-1,terget)

arr=[1,4,6,8,55,88,99]
result=search(arr,0,6,99)
print(result)

