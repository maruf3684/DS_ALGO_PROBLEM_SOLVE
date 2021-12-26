arr = [8,4,1,5,9,2]

for i in range(1,arr.__len__(),1):
    temp=arr[i]
    j=i-1
    while((j>=0) and (temp>arr[j])):
        arr[j+1]=arr[j]
        j-=1
    arr[j+1]=temp
        
print(arr)