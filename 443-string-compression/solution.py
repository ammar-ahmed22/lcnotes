from typing import List

class Solution:
    def compress(self, chars: List[str]) -> int:
        l = r = k = 0
        while r < len(chars):
            while r < len(chars) and chars[l] == chars[r]:
                r += 1

            chars[k] = chars[l]
            k += 1
            if r - l > 1:
                for c in str(r - l):
                    chars[k] = c
                    k += 1
            l = r
        return k

        



if __name__ == "__main__":
    # Include one-off tests here or debugging logic that can be run by running this file
    # e.g. print(solution.two_sum([1, 2, 3, 4], 3))
    solution = Solution()
