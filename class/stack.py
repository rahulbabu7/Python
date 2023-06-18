class Stack:
    def __init__(self):
        self.stack = [] #!list created

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if len(self.stack) == 0:
            print("Stack is empty.")
        else:
            return self.stack.pop()

    def display(self):
        if len(self.stack) == 0:
            print("Stack is empty.")
        else:
            print("Stack elements:")
            for item in reversed(self.stack):
                print(item)

    # def is_empty(self):
    #     return len(self.stack) == 0


# Example usage
stack = Stack()

stack.push(10)
stack.push(20)
stack.push(30)

stack.display()

popped_item = stack.pop()
print("Popped item:", popped_item)

stack.display()
