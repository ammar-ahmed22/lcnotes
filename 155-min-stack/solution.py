class MinStack:

    def __init__(self):
        self.min_stack = []
        self.stack = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)

        if val <= self.getMin() or not self.min_stack:
            self.min_stack.append(val)
        

    def pop(self) -> None:
        if self.min_stack and self.min_stack[-1] == self.stack[-1]:
            self.min_stack.pop()
        self.stack.pop()
        

    def top(self) -> int:
        return self.stack[-1] # will always be called on non-empty stack
        

    def getMin(self) -> int:
        if self.min_stack:
            return self.min_stack[-1]
        return self.top()
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()



if __name__ == "__main__":
    # Include one-off tests here or debugging logic that can be run by running this file
    # e.g. print(solution.two_sum([1, 2, 3, 4], 3))
    obj = MinStack()
