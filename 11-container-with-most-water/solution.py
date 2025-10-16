from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r, maxArea = 0, len(height) - 1, 0

        while l < r:
            w = r - l
            h = min(height[l], height[r])
            maxArea = max(maxArea, w * h)
            if height[l] > height[r]:
                r -= 1
            else:
                l += 1


        return maxArea
        



if __name__ == "__main__":
    # Include one-off tests here or debugging logic that can be run by running this file
    # e.g. print(solution.two_sum([1, 2, 3, 4], 3))
    solution = Solution()
