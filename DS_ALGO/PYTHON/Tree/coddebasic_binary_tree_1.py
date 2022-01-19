class BinarySeaechTree:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

    def __repr__(self):
        return self.data

    def addChile(self,data):
        if data == self.data:
            return

        if data<self.data:
            if self.left!=None:
                self.left.addChile(data)
            else:
                self.left=BinarySeaechTree(data)

        if data>self.data:
            if self.right!=None:
                self.right.addChile(data)
            else:
                self.right=BinarySeaechTree(data)

    def in_order_traversal(self):
        element=[]
        
        #visit left tree
        if self.left:
            element+=self.left.in_order_traversal()

        #visit base node
        element.append(self.data)

        #visit right tree
        if self.right:
            element+=self.right.in_order_traversal()

        return element

    def searchx(self,val):
        if self.data==val:
            return True

        if val<self.data:
            if self.left:
                return self.left.searchx(val)
            else:
                return False

        if val>self.data:
            if self.right:
                return self.right.searchx(val)
            else:
                return False
     


#helper function
def build_tree(elements):
    root=BinarySeaechTree(elements[0])

    for i in range(1,len(elements)):
        root.addChile(elements[i])
    return root
        


if __name__ == '__main__':
    numbers=[17,4,1,20,9,23,18,34]
    numbers_tree=build_tree(numbers)

    print(numbers_tree.in_order_traversal())    
    print(numbers_tree.searchx(10))
