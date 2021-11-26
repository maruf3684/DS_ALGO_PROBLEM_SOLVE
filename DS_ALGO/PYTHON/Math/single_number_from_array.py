
##! find single number from a given array

# arr=[1,1,2,2,3,4,4]
# arr=sorted(arr)
# print(arr)
# star=False
# for i in range(0,len(arr),2):
#     if star ==False and i==len(arr)-1:
#         print("thr number is" ,arr[i])
#     for j in range(i+1,len(arr),1):
#         if arr[i]==arr[j]:
#             break
#         else:
#             print("the number iss" , arr[i])
#             star=True
#             break

##! with bitwise xor
#a xor 1= ulta a
#a xor 0=a
# a xor a =0


def checksingle(arr):
    unique=0
    for i in arr:
        unique=unique ^ i
    return unique

arr=[1,1,2,2,4,3,5,9,5,9,4]
#arr=sorted(arr)
print(arr)
print(checksingle(arr))



print()

