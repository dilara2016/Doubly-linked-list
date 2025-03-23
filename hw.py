class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLL:
    def __init__(self):
        self.head = None

    def insert_beg(self,data):
        #new node
        nb = Node(data)
        if self.head is None: #checking if list empty
            self.head = nb
        else:
            nb.next = self.head
            nb.head.prev =nb
            self.head = nb
    
    def insert_end(self,data):
        ne = Node(data)
        if self.head is None:
            self.head = ne
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = ne
            ne.prev = temp

    def delete_beg(self):
        if self.head is None:
            print("List is empty")
        else:
            temp = self.head
            if self.head.next is None:
                self.head =None
            else:
                self.head = self.head.next
                self.head.prev = None
            temp = None

    def delete_end(self):
        if self.head is None:
            print("List is empty")
        else:
            if self.head.next is None:
                self.head = None
            else:
                temp = self.head
                while temp.next:
                    temp = temp.next
                temp.prev.next = None
                temp = None

    def display(self):
        if self.head is None:
            print("List is empty")
        else:
            temp = self.head
            while temp:
                print(temp.data,"-->", end=" ")
                temp = temp.next
            print("None")
            
l = DoublyLL()
l.insert_end(10)
l.insert_end(20)
l.insert_end(30)

print("Starting List:")
l.display()

print("\nInsertion at beg.")
l.insert_beg(100)
l.display()

print("\nInsertion at end.")
l.insert_end(200)
l.display()

print("\nDeletion at beg.")
l.delete_beg()
l.display()

print("\nDeletion at end.")
l.delete_end()
l.display()