from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        maxL, maxR = 0, 0
        l, r = 0, len(height) - 1
        trapped = 0
        
        while l < r:
            maxL, maxR = max(maxL, height[l]), max(maxR, height[r])

            if maxL <= maxR:
                trapped += maxL - height[l]
                l += 1
            else:
                trapped += maxR - height[r]
                r -= 1
        
        return trapped

        



if __name__ == "__main__":
    # Include one-off tests here or debugging logic that can be run by running this file
    # e.g. print(solution.two_sum([1, 2, 3, 4], 3))
    solution = Solution()
