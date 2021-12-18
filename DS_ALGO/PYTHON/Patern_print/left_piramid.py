# my way
def rightPiramid2(n):
    for i in range(0,2*n-1,1):
        if i<n:
            decrese=n-(i+1)
            increse=0
            for j in range(0,n,1):
                if increse<decrese:
                    print(" ",end=' ')
                    increse+=1
                else:
                    print("*",end=' ')
            print("\n",end='')
        else:    
            decrese=n-(2*n-(i+1))
            increse=0
            for k in range(0,n,1):
                if increse<decrese:
                    print(" ",end=' ')
                    increse+=1
                else:
                    print("*",end=' ')
            print("\n",end='')    


rightPiramid2(5)


# efficiant way?