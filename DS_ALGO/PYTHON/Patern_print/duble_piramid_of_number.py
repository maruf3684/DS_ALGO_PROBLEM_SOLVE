

def pattern(n):
    for i in range(1,n*2+1):
        space=(n-i) if i<=n else (i-n)
        for j in range(space):
            print(" ",end='')
        if i<=n:
            for j in range(i,0,-1):
                print(j,end='')

            for j in range(2,i+1):
                print(j,end='')
        else:
            for j in range(2*n-i,0,-1):
                print(j,end='')

            for j in range(2,2*n-i+1):
                print(j,end='')            
    
        print("\n",end='')


pattern(5)