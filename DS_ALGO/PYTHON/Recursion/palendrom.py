
sum=0
def palindrom(n):
    def reverse (n):
        if n==0:
            return
        rem=n%10
        global sum
        sum=sum*10+rem
        reverse(n//10)
    reverse(n)    
    if sum==n:
        return True
    else:
        return False



print(palindrom(121))