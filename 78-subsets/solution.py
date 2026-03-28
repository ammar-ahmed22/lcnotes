from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []
        def recurse(i):
            if i >= len(nums):
                res.append(subset.copy())
                return
            subset.append(nums[i])
            recurse(i + 1)
            subset.pop()
            recurse(i + 1)

        recurse(0)
        return res


if __name__ == "__main__":
    # Include one-off tests here or debugging logic that can be run by running this file
    # e.g. print(solution.two_sum([1, 2, 3, 4], 3))
    solution = Solution()
