#reverse a number 
sum=0
def reverse (n):
    if n==0:
        return
    rem=n%10
    global sum
    sum=sum*10+rem
    reverse(n//10)

reverse(1234)
print(sum)





