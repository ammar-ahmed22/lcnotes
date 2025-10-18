from typing import List

class Solution:
    def evaluate(self, operator: str, a: int, b: int) -> int:
        if operator == "+":
            return a + b
        if operator == "*":
            return a * b
        if operator == "-":
            return b - a
        if operator == "/":
            return int(b / a)
        
        raise ValueError(f"invalid operator: '{operator}'")

    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token == "+" or token == "-" or token == "*" or token == "/":
                a = stack.pop()
                b = stack.pop()
                stack.append(self.evaluate(token, a, b))
            else:
                stack.append(int(token))
        return stack[-1]
        



if __name__ == "__main__":
    # Include one-off tests here or debugging logic that can be run by running this file
    # e.g. print(solution.two_sum([1, 2, 3, 4], 3))
    solution = Solution()
