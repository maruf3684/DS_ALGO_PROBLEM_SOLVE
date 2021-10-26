
class Node:
    def __init__(self,value=None):
        self.value = value
        self.next=None

class SlinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    def insertSll(self,value,position):
        newNode=Node(value)

        if self.head is  None:
            self.head=newNode
            self.tail=newNode
        else:
            if position ==0:
                newNode.next=self.head
                self.head=newNode
            elif position ==1:
                newNode.next=None
                self.tail.next=newNode
                self.tail=newNode
            else:
                index=0
                i=self.head
                while index<position-1:
                    i=i.next
                    index+=1
                newNode.next=i.next
                i.next=newNode
                



if __name__ == "__main__":
    
    single=SlinkedList()

    single.insertSll(1,0)
    single.insertSll(2,0)
    single.insertSll(3,0)
    single.insertSll(4,1)
    single.insertSll(5,1)
    single.insertSll(9,3)
    single.insertSll(7,1)
    single.insertSll(20,4)
 
    # single.insertSll(2,1)
    # single.insertSll(3,1)
    # single.insertSll(4,1)

    print([i.value for i in single])


    
    




