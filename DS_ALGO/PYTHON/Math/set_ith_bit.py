

#! ith bit ke 0 paile 1 kore dau

def onecreate(n,i):
    tempvalue=1<<i-1
    print (n)
    print (bin(n))
    print (bin(tempvalue))
    return bin(n | tempvalue)

print(onecreate(40,3))

#! ith bit ke 1 paile 0 kore dau  
print(".......................")

# def zerocreate(n,i):
#    # tempvalue = 1<<(len(bin(n))-3)
#     mask_len=len(bin(n))-2
#     tempvalue=
#     print (n)
#     print (bin(n))
#     print (bin(tempvalue))


#     return bin(n & tempvalue)

# print(zerocreate(40,3))

