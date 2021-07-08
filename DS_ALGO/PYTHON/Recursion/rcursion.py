
def first():
    second()
    print("I am firsst")


def second():
    third()
    print("I am second")

def third():
    four()
    print("I am third")

def four():
    print("I am four")


first()

#######################################

def first():
    print(second())
    return "I am firsst"


def second():
    print(third())
    return "I am second"


def third():
    print(four())
    return "I am third"


def four():
    return "I am four"


print(first())
