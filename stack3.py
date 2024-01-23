class Stack: #creates the class stack which is work as the real world object
    
    def __init__(self, max_size = 100):  # Here is the constructor which  automatically calls the methods of the class and attributes also
        self.size = max_size # here initialize the 
        self.item = []   #initializes the items of the stack by empty list as the default value
        self.top = -1   #Initializes top as -1 

    def push(self, x):    #Method 1 describes the push operation (Takes 2 arguments i.e. x and self self is parameter and x is actual value which will be inserted in stack)
        
        if self.top >= self.size - 1:  #checks the stack is full or not if full it doesnt insert the any value in stack 
            print("Stack Overflow")    #
            return False
        else:
            self.top += 1
            self.item.append(x)
            print(f"{x} pushed into stack")
            return True

    def pop(self):
        if self.top == -1:
            print("Stack Underflow")
            return 0
        else:
            x = self.item.pop()
            self.top -= 1
            return x

    def peek(self):
        if self.top < 0:
            print("Stack is Empty")
            return 0
        else:
            x = self.item[self.top]
            return x
    def search_value(self,value):
        if self.top == -1:
            print("the stack is empty")
            return 0 
        else:
            '''if self.item[self.top] == value:
                print(f"{value} is present in the stack at {self.top}")
                return'''
            for i in range(self.top, -1, -1):
                if self.item[i] == value:
                    print(f"{value} is present in the stack at position {i}")
                    return

        print(f"The {value} is not present in the stack")
    def display(self):
        if self.top == -1:
            print("the stack is empty")
            return
        else:
            print("the elements present in tha stack are : ")
            for i in range (self.top + 1):
                print(self.item[i], end=" ")
            print()
            
    def user_ip(self):
        max_size = int(input("Enter the size of stack: "))
        self.size = max_size
        for i in range (max_size):
            x = int(input())
            self.push(x)
            
# Example usage:
stack_object = Stack()
stack_object.user_ip()
stack_object.display()

#print("Top element is:", stack_object.peek())
#print(f"{stack_object.pop()} Popped from stack")

# Print top element of stack after popping
#print("Top element is:", stack_object.peek())

#rint("After deletion of top element stack is : ")

#stack_object.display()

value = int(input("Enter the value for search : "))

stack_object.search_value(value)