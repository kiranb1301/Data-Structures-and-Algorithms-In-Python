''' Write a Linked list code which demonstrates a basic operations such as 1. Insertion(At head, End, Middle) 2.Deletion(From head, End, Middle)
    3.) Search a value by index or search a index from value. 4). Display linked list with all the operations.'''
#Create the strucure of Node
class Node:
    def __init__(self, Data):
        self.value = Data
        self.next = None
#create Linked list as per above node format
class LinkedList():
    def __init__(self):
        self.head = None
    
    def insert_at_head(self,value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
    def insert_at_end(self,value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            return
        else:
            current = self.head
            while current.next != None:
                current = current.next
            current.next = new_node
    def insert_at_middle(self, index_val, val): #by element
        new_node = Node(val)
        if self.head == None:
            return
        else:
            current = self.head 
            while current != None:
                if current.value == index_val:
                    new_node.next = current.next
                    current.next = new_node
                    return
                current = current.next
            print("Item is not found")
    def insert_at_index(self, index, value):
        new_node = Node(value)
        if self.head == None:
            return
        elif index == 0:
            new_node.next = self.head
            self.head = new_node
            return
        else:
            current = self.head
            count = 0
            prev = None
            while current != None and count < index:
                prev = current
                current = current.next
                count += 1
            if count == index:
                prev.next = new_node
                new_node.next = current
                return
            else:
                print("Index is out of range")
    def delete_head(self):
        if self.head == None:
            print("the linked list is empty")
        else:
            current = self.head.value
            self.head = self.head.next
            return current
    def delete_end(self):
        if self.head == None:
            print("the Linked list is Empty ")
        elif self.head.next == None:
            current = self.head.value
            self.head = None
            return
        else:
            current = self.head
            while current.next.next != None:
                current = current.next
            current.next = None
            return
    def delete_middle(self,value):
        if self.head == None:
            return f" The linked list is Empty "
        
        else:
            current = self.head
            count = 0
            if current.value == value:
                self.head = self.head.next
                current = None
                print(f"the value deleted from {count}")
                return
            prev = None
            while current != None:
                if current.value == value:
                    prev.next = current.next
                    current = None
                    print(f"the value  is deleted  from  index {count}")
                    return
                prev = current    
                current = current.next
                count += 1
            
        print("the element you enterd are not present in the linked list")
        return
    
            
    def delete_middle1(self,index):
        if self.head == None:
            return f" The linked list is Empty "
        elif index == 0:
            self.head = self.head.next
            print(f"the value deleted from index {index} is {self.head}")
            return
        else:
            current = self.head
            prev = None
            count = 0
            while current.next != None and count < index:
                prev = current
                current = current.next
                count += 1
            if count == index:
                prev.next = current.next
                print(f"the element deleted from  {index} is  {current.value} ")
            else:
                print(f"The {index} is out of range")
    def search_by_value(self, value):
        if self.head == None:
            return f"The linked list is Empty"
        else:
            current = self.head
            count = 0
            if current.value == value:
                print(f"the Value is present at the Head {(count)} Position")
                return
            while current != None:
                if current.value == value:
                    print(f"the {value} is present at the index {count} position in Linked list")
                    return
                current = current.next
                count += 1
        print("The value is not present in Linked list")
        return
    def search_by_index(self, index):
        if self.head == None:
            return f"The linked list is empty"
        else:
            current = self.head
            count = 0
            while current.next != None and count < index:
                    current = current.next
                    count += 1
            if count == index:
                    print(current.value," is present at above index ", index)
                    return
            print("The index is out of Linked list")
            return
    def display_LL(self):
        current = self.head 
        while current != None:
            print(current.value, end=" |->| ")
            current = current.next
        print("None")
def user_ip():
    LL = LinkedList()
    n = int(input(" Enter the Number of Node is Linked list : "))
    print("Enter the elements : ")
    for i in range (0, n):
        data = int(input())
        LL.insert_at_head(data)
    return LL
            
def main():
        
        #Create linked list and insert the value at begining by user.
    ObjLL = user_ip()
    print("The linked list after insertion of elements at head : ")
    ObjLL.display_LL()
        
        # After insertion by ser at the head again it would be insert at the tail(end).
    val = int(input("Enter the element to insert at the end :"))
    ObjLL.insert_at_end(val)
    print("The linked list after insertion of elements at the end : ")
    ObjLL.display_LL()
        
        #Now Insert the Element after the value at any index position
    position = int(input("enter the item : "))
    val = int(input())
    ObjLL.insert_at_middle(position,val)
    print("The linked list after insertion of elements after the given value : ")
    ObjLL.display_LL()

    #Now insert after any index in linked list.
    position1 = int(input("enter the index : "))
    val1 = int(input())
    ObjLL.insert_at_index(position1,val1)
    print("The linked list after insertion of elements at the given index : ")
    ObjLL.display_LL()

    # Delete the node from head of the linked list until it would be Empty.
    print("The linked list after deletion of elements from head : ")
    current = ObjLL.delete_head()
    print(f"the linked list after deletion  : {current} ")
    ObjLL.display_LL()
    
    #Delete node from end of linked list.
    print("the linked list after deletion of element from end : ")
    ObjLL.delete_end()
    ObjLL.display_LL()
            
    #Delete the value from linked list from any index posiition
    value = int(input("Enter the value which you want to delete from linked list"))
    ObjLL.delete_middle(value)
    ObjLL.display_LL()
        
    #Delete the index position from linked list
    index = int(input())
    ObjLL.delete_middle1(index)
    ObjLL.display_LL()
        
    #Search  by given Value at which index position it appears
    value = int(input())
    ObjLL.search_by_value(value)
    ObjLL.display_LL()
        
    # Search value from given index position i.e which value appears at the given index
    index = int(input())
    ObjLL.search_by_index(index)
    ObjLL.display_LL()

main()




        


