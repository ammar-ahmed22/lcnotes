from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        for i in range(len(nums)):
            map[nums[i]] = i

        for i in range(len(nums)):
            curr = nums[i]
            complement = target - curr
            if complement in map and map[complement] != i:
                return [map[complement], i]

        print("should not get here, check testcases")
        return [0, 0]
        



if __name__ == "__main__":
    # Include one-off tests here or debugging logic that can be run by running this file
    # e.g. print(solution.two_sum([1, 2, 3, 4], 3))
    solution = Solution()
