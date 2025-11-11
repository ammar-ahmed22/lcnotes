from typing import List

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0
        for i in range(len(heights) + 1):
            curr = heights[i] if i < len(heights) else 0 # sentinel height of 0 to flush the stack
            while stack and curr < heights[stack[-1]]:
                h_idx = stack.pop()
                h = heights[h_idx]
                left_idx = stack[-1] if stack else -1
                w = i - left_idx - 1
                max_area = max(max_area, h * w)
            stack.append(i)

        return max_area
        



if __name__ == "__main__":
    # Include one-off tests here or debugging logic that can be run by running this file
    # e.g. print(solution.two_sum([1, 2, 3, 4], 3))
    solution = Solution()
