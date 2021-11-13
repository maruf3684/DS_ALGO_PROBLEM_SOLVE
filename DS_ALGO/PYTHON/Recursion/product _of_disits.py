

def prodOfDesits(n):
    if n%10==n:
        return n
    return n%10 * prodOfDesits(n//10)



if __name__=='__main__':
    print(prodOfDesits(13450))