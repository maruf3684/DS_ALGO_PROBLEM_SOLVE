

def reversed(number):
    ans=0
    while number>0:
        rem=number % 10
        rest=number//10
        ans=ans*10+rem 
        number=rest
    return ans

ans=reversed(1234)
print (ans)