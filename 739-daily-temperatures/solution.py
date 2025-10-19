from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        result = [0] * n 
        # Space: O(n)
        stack = []
        # Time: O(n)
        for i in range(n):
            curr = temperatures[i]
            while stack and stack[-1][0] < curr:
                _, prev_i = stack.pop()
                result[prev_i] = i - prev_i
            stack.append((curr, i))
        return result
        



if __name__ == "__main__":
    # Include one-off tests here or debugging logic that can be run by running this file
    # e.g. print(solution.two_sum([1, 2, 3, 4], 3))
    solution = Solution()
