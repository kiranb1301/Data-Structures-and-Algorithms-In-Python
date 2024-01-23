class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
        self.prev = None
class DLL:
    def __init__(self):
        self.head = None
    def insert_head(self,value):
        New_node = Node(value) #step 1 create obj of Node class for insertion
        New_node.next = self.head # link the next of new_node to the current node 
        New_node.prev =  None # assign the prev of new_node as None becoz it will be head node after insertion at beginning of linked list
        if self.head != None:  # check that linked list is empty or not if not, then assign prev of head node to next of new_node
            self.head.prev = New_node
        self.head = New_node  #else head node will be
    def insert_at_end(self,value):
        New_node = Node(value)
        #New_node.next = None
        if self.head == None:
            New_node.prev = None
            self.head = New_node
            return
        else:
            current = self.head
            while current.next != None:
                current = current.next
            current.next = New_node
            New_node.prev = current
    def insert_after_element(self, prev_ele, Value):
        New_node = Node(Value)  #create new_node object of class Node and make asssign the value to that name 
        if self.head == None:    #checks that is linked list is empty or not 
            return f"Linked list is Empty"
        current = self.head       # Initialize the head node as current node
        while current != None:   # now traverse the linked list to check the element where we have to enter the new_node
            if current.value == prev_ele:  # during traversal checks that the if current elemnts value is equal to the given value or not if yes then
                New_node.next = current.next  # Assign the next pointer of the new node to the current nodes next part or next node
                current.next = New_node       # and next of the current node will reference to the new_node
                New_node.prev = current       # and prev of new_node will points to the current node
            if New_node.next != None:          # now checks that if new_node is last node of linked list or not if not
                New_node.next.prev = New_node #  assign the previous of next node of new_node to new_node
                return
            current = current.next
        else:
            print(f"The elemnt is out of range")
    def insert_before_element(self, Pos_node, value):
        New_node = Node(value)
        if self.head == None:
            print("the linked list is empty")
            return
        current = self.head
        while current != None:
            if current.value == Pos_node:
                New_node.prev = current.prev
                New_node.next = current
                current.prev = New_node
                if New_node.prev != None:
                    New_node.prev.next = New_node
                else:
                    self.head = New_node
                return
            current = current.next
        else:
            print(f"the {Pos_node} is out of range")
        
    def insert_before_index(self, Pos_index, value):
        New_node = Node(value)
        if self.head == None:
            print("the linked list is empty")
            return
        if Pos_index == 0:
            New_node.next = self.head 
            self.head = New_node
            return
        current = self.head
        count = 0
        while current != None: 
            if count == Pos_index:
                New_node.prev = current.prev
                New_node.next = current
                current.prev = New_node
                if New_node.prev != None:
                    New_node.prev.next = New_node
                else:
                    self.head = New_node
                return   
            current = current.next
            count += 1
        else:
            print(f"the {Pos_index} is out of range")
    def delete_head(self):
        if self.head == None:
            return f" The linked list is empty"
        else:
            self.head = self.head.next 
            self.head.prev = None
            return
    def delete_end(self):
        if self.head == None:
            return f" The linked list is empty"
        elif self.head.next == None:
            self.head = None
            self.head.prev = None
        else:
            current = self.head
            while current.next.next != None:
                current = current.next
            current.next = None
    def delete_value_DLL(self,value):
        if self.head == None:
            return f"The Doublt linked list is Empty"
        else:
            #current = self.head
            if self.head.value == value:
                self.head = self.head.next
                self.head.prev = None
                return
            prev = None
            current = self.head
            while current != None:
                if current.value == value:
                    prev.next = current.next
                    current.prev = prev
                    current = None
                    return
                prev = current
                current = current.next
            
        print(f"The {value} is not found in doubly linked list")
        return
    def delete_indexval_DLL(self, index):
        if self.head == None:
            return f"The doubly linked list is Empty"
        else:
            current = self.head
            count = 0
            if index == 0:
                self.head = self.head.next
                self.head.prev = None
                print(f"The {current.value} deleted from {count} ")
                return
            current = self.head
            prev = None
            while current != None:
                if count == index:
                    prev.next = current.next
                    current.prev = prev
                    print(f"the {current.value} deleted from the index {count}")
                    return
                prev = current
                current.prev = prev
                current = current.next
                count += 1
                
        print(f" {index} is out of DLL")   
        return  
    def display(self):
        current = self.head
        while current != None:
            print("|",current.value, end=" |<-->| ")
            current = current.next
        print("None |")
    
Linked = DLL()
Linked.insert_at_end(15)
Linked.insert_at_end(30)
Linked.insert_at_end(45)
Linked.insert_at_end(60)
Linked.insert_at_end(75)
Linked.insert_at_end(90)
Linked.display()

Linked.insert_head(5)
print("the Doubly linked list after insertion of new node at head of linked list : ")
Linked.display()


pos = int(input("Enter the element for insertion: "))
val = int(input("Enter the value : "))
Linked.insert_after_element(pos,val)
Linked.display()

pos_node = int(input("Enter the element for insertion: "))
val = int(input("Enter the value : "))
Linked.insert_before_element(pos_node,val)
Linked.display()

pos_index = int(input("Enter the element for insertion: "))
val = int(input("Enter the value : "))
Linked.insert_before_index(pos_index,val)
Linked.display()

Linked.delete_head()
print("the doubly  linked list after deletion of head is : ")
Linked.display()

print("The doubly  Linked list after deletion of end is : ")
Linked.delete_end()
Linked.display()

val = int(input("Enter the value which u want to delete from Doubly linked list : "))
Linked.delete_value_DLL(val)
print(f"the doubly Linked list after deletion of {val}")
Linked.display()

indexval = int(input("Enter the value which u want to delete from Doubly linked list : "))
Linked.delete_indexval_DLL(indexval)
print(f"the doubly Linked list after deletion of value from  given  index {indexval}")
Linked.display()

print(id(Linked.insert_at_end(15)))
print(id(Linked.insert_at_end(30)))
print(id(Linked.insert_at_end(45)))
print(id(Linked.insert_at_end(60)))
print(id(Linked.insert_at_end(75)))
print(id(Linked.insert_at_end(90)))
