class Linkedlist:
    head=None
    tail=None
    size=0

    def insertFirst(self,value):
        node=self.Node()
        node.setValue(value)
        node.next=self.head
        self.head=node

        if self.tail==None:
            self.tail=self.head
        self.size+=1

    def insertLast(self,value):
        if self.tail==None:
            self.insertFirst(value)
            self.size+=1
        else:
            node=self.Node()
            node.setValue(value)
            self.tail.next=node
            self.tail=node
            self.size+=1

    def insert(self,value,index=None):
        if index==1:
            self.insertFirst(value)
            return

        elif(index > 1 and index<=self.size):
            temp=self.head
            for i in range(1,index-1,1):
                temp=temp.next
            node=self.Node()
            node.setValue(value)
            node.next=temp.next
            temp.next=node
            self.size+=1
            return
        elif(index>self.size):
            self.insertLast(value)
            return
        else:
            print ("There is no index number ",index)
   
   
    def deleteFirst(self):
        if self.size==1:
            self.head=None
            self.tail=None
        else:
            self.head=self.head.next
        self.size-=1

    def deleteLast(self):
        if self.size==1:
            self.head=None
            self.tail=None
        else:
            temp=self.head
            for i in range(1,self.size-1,1):
                temp=temp.next
            
            self.tail=temp
            self.tail.next=None
        self.size-=1
        return

    def delete(self,index):
        if self.size==1:
            self.head=None
            self.tail=None
            return
        if index==1:
            self.deleteFirst()
        elif (index==self.size):
            self.deleteLast()
        else:
            temp=self.head
            for i in range(1,index-1,1):
                temp=temp.next
            temp.next=temp.next.next
        self.size-=1


    def display(self):
        temp=self.head
        while(temp):
            print(temp.value,"-->",end='')
            temp=temp.next
        print("\n",end='')


    def get(self,index):
        if index >0 and index <=  self.size:
            temp=self.head
            for i in range(1,index,1):
                temp=temp.next
            print(temp.value)
        else:
            print("Link list out of bound")


    class Node:
        value=None
        next=None

        def setValue(self,value):
            self.value=value


list=Linkedlist()

list.insertFirst(5)
list.insertFirst(6)
list.insertFirst(4)
list.insertFirst(3)
list.display()

list.insertLast(8)
list.insertLast(9)
list.display()

print (list.size)

list.deleteLast()
list.display()
list.deleteLast()
list.display()

list.get(1)
list.get(2)
list.get(3)
list.get(4)
list.get(0)