from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        map = {}
        for num in nums:
            if num in map:
                return True
            map[num] = True

        return False
        



if __name__ == "__main__":
    # Include one-off tests here or debugging logic that can be run by running this file
    # e.g. print(solution.two_sum([1, 2, 3, 4], 3))
    solution = Solution()
