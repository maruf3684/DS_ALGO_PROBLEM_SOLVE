def numIdenticalPairs(nums):
    dict={}
    count=0
    for val in nums:
        if val not in dict:
            dict[val]=1
        else:
            count+=dict[val]
            dict[val]=dict[val]+1
    return count
            
        
print(numIdenticalPairs( [1,2,3,1,1,3]))