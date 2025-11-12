from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0
        max_p = 0
        b, s = 0, 1
        while s < len(prices):
            profit = prices[s] - prices[b]
            if profit > 0:
                max_p = max(max_p, profit)
            else:
                b = s
            s += 1
        return max_p
        



if __name__ == "__main__":
    # Include one-off tests here or debugging logic that can be run by running this file
    # e.g. print(solution.two_sum([1, 2, 3, 4], 3))
    solution = Solution()
