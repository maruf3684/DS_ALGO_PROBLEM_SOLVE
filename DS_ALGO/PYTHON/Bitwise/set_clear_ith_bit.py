
#!change position 3 (0 to 1) that means set position 3

n=0b100110100

def findbit(n,i):
    mask=1<<i
    result=n|mask
    return result


print("pos 4", bin(findbit(n,3)))

print(bin(n))




#!change position 2 (1 to 0) that means clear position 2

n=0b100110100

def findbit(n,i):
    mask=1<<i
    mask=~mask
    result=n&mask
    return result

print("pos 4", bin(findbit(n,2)))

print(bin(n))
