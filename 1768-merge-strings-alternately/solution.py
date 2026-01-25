from typing import List

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i = j = k = 0

        res = ""
        while i < len(word1) and j < len(word2):
            if k % 2 == 0:
                res += word1[i]
                i += 1
            else:
                res += word2[j]
                j += 1
            k += 1

        while i < len(word1):
            res += word1[i]
            i += 1

        while j < len(word2):
            res += word2[j]
            j += 1

        return res


if __name__ == "__main__":
    # Include one-off tests here or debugging logic that can be run by running this file
    # e.g. print(solution.two_sum([1, 2, 3, 4], 3))
    solution = Solution()
