arr=[3,5,3,6,7,3,2,156,89,66,12]

for i in range(1, len(arr)):
    
    key = arr[i]

    j = i-1
    
    while j >= 0 and key < arr[j] :
            arr[j + 1] = arr[j]
            j -= 1
    arr[j + 1] = key

print(arr)