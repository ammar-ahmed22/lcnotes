from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        l, r = 0, n - 1

        while l <= r:
            m = (l + r) // 2
            if (m == 0 or nums[m - 1] > nums[m]) and (m == n - 1 or nums[m + 1] > nums[m]):
                return nums[m]
            elif nums[r] < nums[m]:
                # move towards smaller value
                l = m + 1
            else:
                # move towards smaller value
                r = m - 1
        return -1 # shouldn't get here
        



if __name__ == "__main__":
    # Include one-off tests here or debugging logic that can be run by running this file
    # e.g. print(solution.two_sum([1, 2, 3, 4], 3))
    solution = Solution()
