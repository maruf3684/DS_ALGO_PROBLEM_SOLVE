
#my way
def rightPiramid(n):
    for i in range(0,2*n,1):
        if i<=n:
            for j in range(0,i,1):
                print("*",end=' ')
        else:
            for j in range(0,2*n-i,1):
                print("*",end=' ')
            
          
        print("\n",end='')


rightPiramid(5)

# efficiant way
def rightPiramid2(n):
    for i in range(0,2*n,1):
        terget = i if i < n else 2*n-i
        for j in range(0,terget,1):
            print("*",end=' ')
          
        print("\n",end='')


rightPiramid2(5)
