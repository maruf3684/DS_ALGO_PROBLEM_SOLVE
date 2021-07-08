

# def powerof(n):
#     i=0
#     power =1
#     while (i<n):
#         power=power*2
#         i=i+1
#     return power
#
# print(powerof(4))


def powerof(n):
    if (n==0):
        return 1
    else:
        power=powerof(n-1)
        return power*2

print(powerof(3))