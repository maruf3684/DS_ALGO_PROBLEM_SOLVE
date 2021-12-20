
def pattern(n):
    for i in range(1,n+1):
        space=(n-i)
        for j in range(space):
            print(" ",end='')
        
        for j in range(i,0,-1):
            print(j,end='')

        for j in range(2,i+1):
            print(j,end='')
    
        print("\n",end='')


pattern(5)