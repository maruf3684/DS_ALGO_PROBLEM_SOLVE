#Given an array A of size N. You need to find the sum of Maximum and Minimum element in the given array.


def maxmin(A):
    max=A[0]
    min=A[0]
    for i in range(len(A)-1):
        if min>A[i]:
            min=A[i]

    for i in range(len(A)-1):
        if max<A[i]:
            max=A[i]
    return max+min



A = [-2, 1, -4, 5, 3]
A = [1, 3, 4, 1]
print(maxmin(A))