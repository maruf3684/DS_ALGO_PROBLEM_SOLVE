
#!factorial of 3

number=3
n=number
for i in range(n-1):
    n=n-1
    number=number*n
    
print(number)


#!recursive way

def factorial(n):
    if n==1:
        return 1
    return n*factorial(n-1)

ans=factorial(3)
print(ans)