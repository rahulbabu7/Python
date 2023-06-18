class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            print("Stack is empty.")

    def display(self):
        if not self.is_empty():
            print("Stack elements:")
            for item in reversed(self.stack):
                print(item)
        else:
            print("Stack is empty.")

    def is_empty(self):
        return len(self.stack) == 0


# Example usage
stack = Stack()

stack.push(10)
stack.push(20)
stack.push(30)

stack.display()

popped_item = stack.pop()
print("Popped item:", popped_item)

stack.display()
