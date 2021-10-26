#find the first and last position of terget



    

def Search(arr,terget,side):
    start = 0
    end=len(arr)-1

    while (start<end):
        mid=(start+end)//2

        if(terget<arr[mid]):
            end=mid-1
        elif(terget>arr[mid]):
            start=mid+1
        elif(terget==arr[mid]):
            #potential ans found
            var=mid
            if(side==True):
                end=mid-1
            else:
                start=mid+1
    return var

   
arr=[1,2,3,5,5,5,5,5,5,5,5,5,5,7,8,9,66]

first=Search(arr,5,True)
last=Search( arr,5,False)

ans=[first,last]
print(ans)