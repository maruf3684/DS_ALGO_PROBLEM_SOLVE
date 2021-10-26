class TreeNode:
    def __init__(self,data,children=[]):
        self.data = data
        self.children = children

    def __str__(self,level=0):
        ret = " "*level+str(self.data)+"\n"   ## it's an string
        for child in self.children:
            ret+=child.__str__(level+1)
        return ret

    def add_child(self,porertuk):
        self.children.append(porertuk)



if __name__ == '__main__':
    tree = TreeNode('Drinks',[])

    cold = TreeNode('Cold',[])
    hot = TreeNode('Hot',[])

    tree.add_child(cold)
    tree.add_child(hot)


    cola=TreeNode('Cola',[])
    fanta=TreeNode('Fanta',[])
    cold.add_child(cola)
    cold.add_child(fanta)

    print (tree)