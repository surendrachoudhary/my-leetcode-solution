class MyStack:
    def __init__(self):
        """
        Initialize two deques to represent the stack.
        """
        self.q1 = deque()
        self.q2 = deque()

    def push(self, x: int) -> None:
        """
        Pushes an element onto the stack.
        """
        self.q1.append(x)

    def pop(self) -> int:
        """
        Removes and returns the element at the top of the stack.
        """
        if not self.empty():  # Check if the stack is not empty
            return self.q1.pop()  # Remove and return the top element from q1
        else:
            return None  # Return None if the stack is empty

    def top(self) -> int:
        """
        Returns the element at the top of the stack without removing it.
        """
        return self.q1[-1]  # Return the last element of q1

    def empty(self) -> bool:
        """
        Checks whether the stack is empty.
        """
        return len(self.q1) == 0  # Return True if q1 is empty, otherwise False

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
