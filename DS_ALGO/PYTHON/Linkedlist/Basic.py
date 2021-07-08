
class Node:
    def __init__(self,data=None,next=None):
        self.data = data
        self.next=next
############################################################

class Linkedlist:
    def __init__(self):
        self.head=None

    def insert_at_begin(self,data):
        node=Node(data,self.head)
        self.head=node
    
    def insert_at_end(self,data):
        if self.head is None:
            node=Node(data,None)
            self.head=node
            return
        itr=self.head
        while itr.next:
            itr=itr.next
        node=Node(data,None)
        itr.next=node
    
    def createList(self,data_list):
        self.head=None
        for i in data_list:
            self.insert_at_end(i)

    def get_length(self):
        count=1
        itr=self.head
        while itr.next:
            count+=1
            itr=itr.next
        return count

  
    def remove_at(self, index):
        if index<0 or index>=self.get_length():
          raise Exception("Invalid Index")

        if index==0:
            self.head = self.head.next
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                break

            itr = itr.next
            count+=1

    def insert_at(self, index, data):
        if index<0 or index>self.get_length():
            raise Exception("Invalid Index")

        if index==0:
            self.insert_at_begining(data)
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                node = Node(data, itr.next) ##null value soho node banacche
                itr.next = node
                break

            itr = itr.next
            count += 1


    def prints(self):
        itr=self.head
        llstr=""
        while itr:
            llstr=llstr+str(itr.data)+"-->"
            itr=itr.next
        print(llstr)


    

if __name__ == '__main__':
    mylist=Linkedlist()
    mylist.insert_at_begin(2)
    mylist.insert_at_begin(4)
    mylist.insert_at_begin(6)
    mylist.insert_at_begin(66)
    mylist.prints()
########################################## insert at end
    mylist.insert_at_end(1)
    mylist.insert_at_end(5)
    mylist.insert_at_end(7)
    mylist.prints()
################################################### createlist
    mylist.createList([1,5,3,7,9,4,333])
    mylist.prints()
###################################################### get get_length
    print(mylist.get_length())
############################################################ remove at
    mylist.remove_at(4)
    mylist.prints()

############################################################### insert at
    mylist.insert_at(2,999)
    mylist.prints()
###################################### insert at
    mylist.insert_at(7,9998)
    mylist.prints()