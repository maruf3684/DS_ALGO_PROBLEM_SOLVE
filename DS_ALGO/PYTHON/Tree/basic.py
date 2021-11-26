class Node(object):
    def __init__(self,data):
        self.data = data
        self.left=None
        self.right=None

    def __repr__(self):
        return "node:{},data:{}".format("Root",self.data)
        return repr(self.data)

    def add_left(self,node):
        self.left = node

    def add_right(self,node):
        self.right =node
    



def create_tree():
    two=Node(2)
    seven=Node(7)
    nine=Node(9)

    two.add_left(seven)
    two.add_right(nine)

    one=Node(1)
    six=Node(6)
    seven.add_left(one)
    seven.add_right(six)

    five=Node(5)
    ten=Node(10)
    six.add_left(five)
    six.add_right(ten)

    eight=Node(8)
    nine.add_right(eight)

    three=Node(3)
    four=Node(4)
    eight.add_left(three)
    eight.add_right(four)

    return two #its root node

def pre_order(node):
    print (node)
    if node.left:
        pre_order (node.left)

    if node.right:
        pre_order (node.right)

def post_order(node):
    if node.left:
        post_order (node.left)
    
    if node.right:
        post_order (node.right)
    print (node)


def in_order(node):
    if node.left:
        in_order (node.left)
    print (node)

    if node.right:
        in_order (node.right)


#!preorder a 1at a print//post order a last a print// in order a majhe p[rint lagabo





if __name__ == '__main__':
    root = create_tree()
    print(root)
    print("--------------------------------")
    pre_order (root)
    print("--------------------------------")
    post_order (root)
    print("--------------------------------")
    in_order (root)

