#findh ith bit of a number of
#40=101000

def findBit(n,i):
    print("value of leftsift",bin(1<<i-1))
    pre=1<<(i-1)
    cal=n & pre
    if pre==cal:
        return f"{i} th bit is 1"
    return f" {i} th bit is 0 {bin(cal)}" 

print(findBit(40,4))

