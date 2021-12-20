
#n2 time complexity
arr=[0,8,4,12,2,10,6,14,1,9,5,13,3,11,7,15]
dp=[]

for i in range(len(arr)):
    dp.append(1)

for i in range(1,len(arr)):
    for j in range(0,i):
        if(arr[j]<arr[i]):
            dp[i]=max(dp[i],dp[j]+1)

print(dp)
print("ans is",max(dp))    

#nlogn time complexity


