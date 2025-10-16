from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        print(f"nums = {nums}")
        i = 0
        ans = []
        # To have at least 3 elements
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            target = nums[i] * -1
            l, r = i + 1, len(nums) - 1
            while l < r:
                potential = nums[l] + nums[r]
                if potential == target:
                    ans.append([nums[i], nums[l], nums[r]])
                    while l < r and nums[l] == nums[l + 1]:
                        l += 1
                    while l < r and nums[r] == nums[r - 1]:
                        r += 1
                    l += 1
                    r -= 1
                elif potential < target:
                    l += 1
                else:
                    r -= 1
        return ans
        



if __name__ == "__main__":
    # Include one-off tests here or debugging logic that can be run by running this file
    # e.g. print(solution.two_sum([1, 2, 3, 4], 3))
    solution = Solution()
