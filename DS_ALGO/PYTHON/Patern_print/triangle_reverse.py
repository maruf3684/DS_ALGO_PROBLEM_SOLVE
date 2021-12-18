

#formula 1
def pattern(n):
    for i in range(n,0,-1):
        for j in range(0,i):
            print("*",end=' ')
        print("\n",end='')

pattern(5)
        

#formula 2
def pattern2(n):
    for i in range(0,n+1):
        for j in range(0,n-i,1):
            print("*",end=' ')
        print("\n",end='')

pattern2(5)
        
