


A = A = [1, 2, 3, 4, -11 ,2, 3, 4, 2, 7,-30,50]

def maxSubArray(A):
    sm=mainsum=A[0]
    for i in range(1,len(A)):
        sm=max((sm+A[i]),A[i])

        if (sm>mainsum):
            mainsum=sm
    return mainsum

print (maxSubArray(A))