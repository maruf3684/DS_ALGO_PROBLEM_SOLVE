
arr=[4,1,9,2,3,6]

for i in range(arr.__len__()-1):
    min=i
    for j in range(i,arr.__len__(),1):
        if(arr[j]<arr[min]):
            min=j
    if (arr[min]!=arr[i]):
        arr[i], arr[min]=arr[min], arr[i]     
        

print(arr)
        
