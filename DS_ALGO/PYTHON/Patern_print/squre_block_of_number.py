
def pattern(n):
    for i in range(1,n):
        for j in range(1,n):
            dist_up=i
            dist_down=n-i
            dist_left=j
            dist_right=n-j
            result=min(dist_up,dist_down,dist_left,dist_right)
            print(result,end=" ")
        print("\n",end="")

pattern(10)


print("pattern number 2")


def pattern2(n):
    for i in range(1,n):
        for j in range(1,n):
            dist_up=i
            dist_down=n-i
            dist_left=j
            dist_right=n-j
            result=n//2-min(dist_up,dist_down,dist_left,dist_right)
            print(result,end=" ")
        print("\n",end="")

pattern2(10)