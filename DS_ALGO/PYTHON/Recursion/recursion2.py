

def lesscounter(n):
    if (n==1):
        print("n is less than 1")
    else:
        lesscounter(n-1)
        print(n)

lesscounter(3)