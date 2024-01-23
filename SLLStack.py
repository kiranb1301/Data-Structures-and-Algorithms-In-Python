class Node:
    def __init__(self,value):
        self.val = value 
        self.next = None
class Singly:
    def __init__(self):
        self.head = None
    def isempty(self):
        if self.head == None:
            return True 
        else:
            return False
    def push(self, value):
        New_node = Node(value)
        if self.head == None:
            self.head = New_node
            print(f"{value} pushed in stack")
            return
        else:
            current = self.head
            while current.next != None:
                current = current.next 
            current.next = New_node
            print(f"{value} pushed in stack")
    def pop(self):
        if self.head == None:
            return False 
        else:
            current = self.head 
            prev = None
            while current.next != None:
                prev = current 
                current = current.next
            prev.next = current.next
            current = None
            return True
    def peek(self):
        if self.isempty() == True:
            print("The stack is empty or underflow")
            return
        else:
            current = self.head
            while current.next != None:
                current = current.next
            return current.val
    def searchval(self, value):
        if self.isempty()  == True:
            print(" The stack is empty or underflow")
            return
        else:
            if self.head == value:
                print(f"the {value} is present at in stack at the {self.head} position ")
            current = self.head
            count = 0
            while current != None:
                if current.val == value:
                    print(f"the {value} is present in stack at the {count} position")
                current = current.next
                count += 1
                
    def display(self):
        current = self.head 
        while current != None:
            print(current.val, end= " ")
            current = current.next
        print()
    def user_ip(self):
        stack_size = int(input("Enter the size of stack : "))
        print("Enter the elements in the stack :")
        for i in range(stack_size):
            data = int(input(f" Enter the value for {i} position: "))
            self.push(data)
        return    
stack = Singly()
stack.isempty()
stack.user_ip()
'''stack.push(5)
stack.push(10)
stack.push(15)
stack.push(20)
stack.push(25)
stack.push(30)'''

print("the Elements presnt in the stack are : ")
stack.display()

value = int(input("Enter the value for search in stack: "))
stack.searchval(value)
stack.display()

top_of_stack = stack.peek()
print(f"the top element of the stack is {top_of_stack}")


stack.pop()
print("the stack after deletio of the top element: ")
stack.display()

top_of_stack = stack.peek()
print(f"the top element of the stack is {top_of_stack}")
