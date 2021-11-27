
##check koro 2 kotobar che

def check(number,val):
    arr=[]
    count=0
    for i in range(0,len(str(number))):
        lastVal=number%10
        restval=number//10
        pos=len(str(number))
        if lastVal==val:
            count+=1
            arr.append(pos)
        number=restval
        pos-=1
    arr.reverse()   
    return count,arr

frequency,position=check(123425677732334272,2)
print(f"2 appered {frequency} times, position={position}")



def check(number,val):
    arr=[]
    count=0
    i=1
    while (number>0):
        pos=len(str(number))
        lastVal=number%10
        if lastVal==val:
            count+=1
            arr.append(pos)
        number=number//10
        i=i+1
        pos-=1
    arr.reverse()
    return count,arr

frequency,position=check(123425677732334272,99)
print(f"2 appered {frequency} times, position={position}")
