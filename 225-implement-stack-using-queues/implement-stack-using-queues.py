class MyStack:

    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()

    def push(self, x: int) -> None:
        self.q1.append(x)

    def pop(self) -> int:
        if not self.empty():
            return self.q1.pop()
        else:
            return None  


    def top(self) -> int:
        return self.q1[-1]

    def empty(self) -> bool:
        if len(self.q1) > 0:
            return False 
        else:
            return True 

        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()