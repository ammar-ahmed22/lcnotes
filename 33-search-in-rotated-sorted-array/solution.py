from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        # Find pivot index (min in rotated sorted)
        l, r = 0, n - 1

        pivot = -1
        while l <= r:
            m = (l + r) // 2
            if (m == 0 or nums[m - 1] > nums[m]) and (m == n - 1 or nums[m + 1] > nums[m]):
                pivot = m
                break
            elif nums[r] < nums[m]:
                l = m + 1
            else:
                r = m - 1

        if pivot == -1:
            raise RuntimeError("pivot index not found, check your implementation")

        # Search in correct side of array
        l, r = 0, n - 1
        if target >= nums[0] and pivot != 0 and target <= nums[pivot - 1]:
            # search from 0 to pivot
            r = pivot - 1
        else:
            # search from pivot to end
            l = pivot
            pass

        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                return m
            elif nums[m] < target:
                l = m + 1
            else:
                r = m - 1
        
        return -1
        



if __name__ == "__main__":
    # Include one-off tests here or debugging logic that can be run by running this file
    # e.g. print(solution.two_sum([1, 2, 3, 4], 3))
    solution = Solution()
