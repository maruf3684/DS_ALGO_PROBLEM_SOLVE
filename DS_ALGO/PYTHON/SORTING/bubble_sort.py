
arr=[3,1,5,4,2]

for i in range(arr.__len__()):
    for j in range(arr.__len__()-1-i):
        if(arr[j]>arr[j+1]):
            arr[j],arr[j+1] = arr[j+1],arr[j]

print(arr)
