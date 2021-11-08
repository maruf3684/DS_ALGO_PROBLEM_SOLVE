
#find fibonacchi number

def fibo(n):
    #base condition for
    if n<2:
        return n
    return fibo(n-1) + fibo(n-2)

print (fibo(4))

