from typing import List
import sys

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        smallest = second_smallest = sys.maxsize
        for num in nums:
            if num <= smallest:
                smallest = num
            elif num <= second_smallest:
                second_smallest = num
            else:
                return True
        return False



if __name__ == "__main__":
    # Include one-off tests here or debugging logic that can be run by running this file
    # e.g. print(solution.two_sum([1, 2, 3, 4], 3))
    solution = Solution()
