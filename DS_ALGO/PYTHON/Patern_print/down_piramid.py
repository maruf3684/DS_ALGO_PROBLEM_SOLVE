def piramid(n):
    star=n-1
    for i in range(1,n//2+1):
        
        space=i-1
        for j in range(0,space):
            print(" ",end='')
        
        for j in range(0,star):
            print("*",end="")
        print("\n",end="")
        star-=2
piramid (10)