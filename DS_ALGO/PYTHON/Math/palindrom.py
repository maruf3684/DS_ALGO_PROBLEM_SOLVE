
#!check palindrom like = aba , racecar



def checkPalin(n):
    given_number=n
    main=0
    while(n>0):
        last_degit=n%10
        remain_degit=n//10
        main=(main*10)+last_degit
        n=remain_degit
    if (given_number==main):
        return "palindrom"
    else:
        return "Not palindrom"

print(checkPalin(101010101)) 



