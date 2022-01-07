
class Linklist:
    head=None
    tail=None
    size=0

    def insertLast (self,val):
        if self.head is None:
            self.newNode = self.__Node(val)
            self.head = self.newNode
            self.tail = self.newNode
        else:
            self.newNode = self.__Node(val)
            self.newNode.prev=self.tail
            self.tail.next = self.newNode
            self.tail = self.newNode
        self.size += 1

    def insertFirst(self,val):
        if self.head is None:
            self.newNode = self.__Node(val)
            self.head = self.newNode
            self.tail = self.newNode
        else:
            self.newNode = self.__Node(val)
            self.newNode.next=self.head
            self.head.prev = self.newNode
            self.head = self.newNode
        self.size += 1

    def insert(self,val,index):
        if self.head is None:
            self.insertFirst(val)
            return
        elif (index<=1):
            self.insertFirst(val)
            return
        elif(index>self.size):
            self.insertLast(val)
            return
        else:
            self.count=self.head
            self.iterator=1
            while (self.iterator<index-1):
                self.count=self.count.next
                self.iterator+=1
            self.newNode = self.__Node(val)
            self.newNode.prev = self.count
            self.newNode.next = self.count.next
            self.count.next.prev = self.newNode
            self.count.next=self.newNode  
        self.size += 1

    def display(self):
        self.count=self.head
        print("head->",end="")
        while (self.count):
            print(self.count.val,"<->",end=" ")
            self.count=self.count.next
        print("<-tail size=",self.size,end="")
        print()
    
    def displayRev(self):
        self.count=self.tail
        print("tail->",end="")
        while (self.count):
            print(self.count.val,"<->",end=" ")
            self.count=self.count.prev
        print("<-head size=",self.size,end="")
        print()



    class __Node: #i made it private
        def __init__(self,val=None,prev=None,next=None):
            self.val = val
            self.prev = prev
            self.next = next




if __name__ == "__main__":

    list1 = Linklist()
    list1.insertFirst(5)
    list1.insertFirst(6)
    list1.insertFirst(7)
    list1.insertFirst(8)
    list1.insertLast(1)
    list1.insertLast(2)

    list1.insert(2,2)
    list1.insert(3,3)
    list1.insert(9,9)
    list1.insert(100,1)


    list1.display()
    # list1.displayRev()
    





    ############################################################################

    # list2 = Linklist()
    # list2.insertFirst(1)
    # list2.insertFirst(2)
    # list2.insertFirst(3)
    # list2.insertFirst(4)
    # list2.display()

    # I have to off acces from outside
    # mok=Linklist._Linklist__Node(4)
    # print(mok.val)

