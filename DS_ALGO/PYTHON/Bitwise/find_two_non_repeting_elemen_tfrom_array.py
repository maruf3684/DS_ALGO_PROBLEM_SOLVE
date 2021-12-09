
#! find two non repeting element from array
arr=[3,4,1,4,3,5,1,9]
#2 tar combind xor ber kori
abxor=0
for i in arr:
    abxor=abxor^i
print("abxor=" ,bin(abxor))
combindans=abxor

#bin a convert kore right most setbit ber kori
count=0
while(abxor&1!=1):
    abxor=abxor>>1
    count+=1
print(bin(abxor),count)

#right most set bit a aktar(a) value 1 ache aktar(b) ar valur 0 ache//sei jonno e setbit ta asche  
# 1 value owala mal gula arr2 te rakhi 
arr2=[]
for i in arr:
    if ((i>>count)&1==1):
        arr2.append(i)
print(arr2)


#finding  b
b=0
for i in arr2:
    b=b^i
b=b^combindans

#finding a 
a=combindans
a=a^b

print("Two values are",a,"and",b)

