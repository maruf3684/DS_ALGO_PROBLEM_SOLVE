
# a and b er moddhe koita bit a omil ache ber koro

a=0b10110
b=0b11011

def find_num_of_bits(a,b):
    DiffrentBits=a^b
    count=0
    
    for i in range(str(bin(b)).__len__()-2):
        findone=DiffrentBits&1
        if findone:
            count+=1
        DiffrentBits=DiffrentBits >>  1 
    return count

print (find_num_of_bits(a,b))



#!2nd formula  (n&(n-1))[3 one owala binary sonkha ke total 0 korte (sonkha&sonkha-1) 3ta & operation lagbe]
a=0b101101001
b=0b110110101

def find_num_of_bits(a,b):
    DiffrentBits=a^b
    count=0
    while(DiffrentBits!=0):
        DiffrentBits=DiffrentBits&(DiffrentBits-1)
        count+=1
    return count

print (find_num_of_bits(a,b))


