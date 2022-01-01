

def finder(n,m):
    if (m==1 or n==1):
        return 1
    return finder(n-1,m)+finder(n,m-1)

print(finder(4,4))