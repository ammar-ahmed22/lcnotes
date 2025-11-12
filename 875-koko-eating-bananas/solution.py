from typing import List
import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)

        while l <= r:
            speed = (l + r) // 2
            # calculating hours for this speed
            hours = 0
            for pile in piles:
                hours += math.ceil(pile/speed)

            if hours > h: # increase speed
                l = speed + 1
            else: # decrease speed
                r = speed - 1

        return l
        



if __name__ == "__main__":
    # Include one-off tests here or debugging logic that can be run by running this file
    # e.g. print(solution.two_sum([1, 2, 3, 4], 3))
    solution = Solution()
