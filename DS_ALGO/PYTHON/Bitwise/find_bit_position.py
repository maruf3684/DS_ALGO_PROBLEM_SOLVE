
#find the ith bit
#print(bin(2).replace("0b", ""))




n=0b100110100

def findbit(n,i):
    temp=1<<i
    result=n&temp
    if result==0:
        return 0
    else: 
        return 1

print("pos 0", findbit(n,0))
print("pos 1", findbit(n,1))
print("pos 2", findbit(n,2))
print("pos 3", findbit(n,3))
print("pos 4", findbit(n,4))
print("pos 5", findbit(n,5))
print("pos 6", findbit(n,6))
print("pos 7", findbit(n,7))
print("pos 8", findbit(n,8))
print(bin(n))