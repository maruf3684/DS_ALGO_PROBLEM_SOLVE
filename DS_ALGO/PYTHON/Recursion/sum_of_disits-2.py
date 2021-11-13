

def numberOfDisits(n):
    if n==0:
        return 0
    return n%10 + numberOfDisits(n//10)



if __name__=='__main__':
    print(numberOfDisits(1345))