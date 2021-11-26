
#!my solution
# a=[-5, 3, 6, 12, 15]
# b=[-12, -10, -6, -3, 4, 10]

# #a=[2, 3, 5, 8]
# #b=[10, 12, 14, 16, 18, 20]
# a.extend(b)
# c=sorted(a)
# median=0

# print(c)


# if len(c)%2==0:
#     first= c[len(c)//2]
#     last=c[(len(c)//2)-1]
#     median=(first+last)/2
# else:
#     median=c[len(c)//2]

# print(median)


#! Efficiant solution


import sys
def findMedian(arra,arrb):
    if len(arra) < len(arrb):
        arra,arrb = arrb,arra

    low=0
    high=len(arra)

    while (low <= high):
        midA=(high+low)//2
        midB=(len(arra)+len(arrb)+1)//2-midA
        print(arra)
        print(arrb)
       # print(f"midA:{midA} val {arra[midA]}, midB:{midB} val {arrb[midB]}")
        
        leftValA=-sys.maxsize if midA==0 else arra[midA-1]
        rightValA=sys.maxsize if midA==len(arra) else arra[midA]
        leftValB=-sys.maxsize if midB==0 else arrb[midB-1]
        rightValB=sys.maxsize if midB==len(arrb) else arrb[midB]

        print(f"leftValA:{leftValA} , rightValA:{rightValA}")
        print(f"leftValB:{leftValB} , rightValB:{rightValB}")

        if(leftValA <= rightValB) and (leftValB <= rightValA):
            if ((len(arra)+len(arrb))%2==0):
                ans=(max(leftValA, leftValB)+min(rightValA, rightValB))/2
                print("median= ",ans)
                break
            else:
                ans=max(leftValA, leftValB)
                print("median= ", ans)
                break
        elif(leftValA > rightValB):
            high=midA-1
        else:
            low=midA+1

# arra=[-5, 3, 6, 12, 15]
# arrb=[-12, -10, -6, -3, 4, 10]
################# ans =3

arra=[2, 3, 5, 8]
arrb=[10, 12, 14, 16, 18, 20]
################# ans =11

#arra=[1,2,3,4,5]
#arrb=[6,7,8,9,10,11]
findMedian(arra,arrb)