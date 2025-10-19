from typing import List

class Solution:
    def backtrack(self, open: int, closed: int, n: int, stack: List[str], result: List[str]):
        if open == closed and closed == n:
            result.append("".join(stack))
            return
        
        if open < n:
            stack.append("(")
            self.backtrack(open + 1, closed, n, stack, result)
            stack.pop()

        if closed < open:
            stack.append(")")
            self.backtrack(open, closed + 1, n, stack, result)
            stack.pop()


    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        stack = []
        self.backtrack(0, 0, n, stack, result)
        return result
        



if __name__ == "__main__":
    # Include one-off tests here or debugging logic that can be run by running this file
    # e.g. print(solution.two_sum([1, 2, 3, 4], 3))
    solution = Solution()
