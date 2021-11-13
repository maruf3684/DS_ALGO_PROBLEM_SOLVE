
#reverse
# def prinnt(n):
#     print(n)
#     if n==0:
#         return 0
#     n=n-1
#     return prinnt(n)

# prinnt(5)

#not reverse
# def prinntrev(n):
#     if n==0:
#         return 0
#     n=n-1
#     prinntrev(n)
#     print(n)

# prinntrev(5)


#both directions
def prinntrev(n):
    if n==0:
        return 0

    print(n)
    prinntrev(n-1)
    print(n)

prinntrev(5)
