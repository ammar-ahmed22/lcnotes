from typing import List

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0
        charSet = set()
        l = 0
        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            max_length = max(max_length, r - l + 1)

        return max_length
        



if __name__ == "__main__":
    # Include one-off tests here or debugging logic that can be run by running this file
    # e.g. print(solution.two_sum([1, 2, 3, 4], 3))
    solution = Solution()
