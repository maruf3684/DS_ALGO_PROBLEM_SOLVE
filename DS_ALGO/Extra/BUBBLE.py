list=[5,1,7,9,12,80,300,0]

for i in range(0,len(list)-1,1):
    swap=False
    for j in range(0,len(list)-1-i,1):
        if(list[j]>list[j+1]):
            temp=list[j]
            list[j]=list[j+1]
            list[j+1]=temp
        if swap==True:
            break
print(list)

        