


#triangle with star
def pattern(n):
    for i in range(1,n):
        for j in range(0,i):
            print("*",end=' ')
        print("\n",end='')

pattern(6)


#triangle with number
def patternNumber(n):
    for i in range(0,n+1):
        for j in range(0,i):
            print(j+1,end=' ')
        print("\n",end='')

patternNumber(5)
