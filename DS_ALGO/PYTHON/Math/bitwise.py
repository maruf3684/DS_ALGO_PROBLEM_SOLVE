# find a number odd or even numbers

def checkeven(n):
    if n & 1==1:
        print (n&1)
        return False
    print (n&1)
    return True

print(checkeven(20))



#