
def pattern(n):
    for i in range(2*n):
        total_cols_in_row=i if i < n else 2*n-i
        space=n-total_cols_in_row
        
        for j in range(space):
            print(" ",end='')

        for j in range(total_cols_in_row):
            print("* ",end='')
        print("\n",end="")



pattern(5)