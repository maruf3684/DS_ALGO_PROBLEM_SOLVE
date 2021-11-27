
#! fibonacchi by loops 0,1,1,2,3,5



def fibo(n):
    first=0
    second=1
    for i in range(3,n+1):
        next=first+second
        first=second
        second=next   
    return next

print(fibo(8))


def fiborecr(n):
    if n==1:
        return 0
    if n==2:
        return 1
    return fibo(n-1)+fibo(n-2)

print(fiborecr(8))


def fibowhile(n):
    first = 0
    second=1
    i=1
    next=0
    while (i<=n-2):
        next=first+second
        first=second
        second=next
        i+=1
    return next

print (fibowhile(8))