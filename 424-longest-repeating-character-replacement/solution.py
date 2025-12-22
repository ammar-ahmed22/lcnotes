class Solution:
    def char2idx(self, c: str) -> int:
        return ord(c) - ord('A')

    def characterReplacement(self, s: str, k: int) -> int:
        freq = [0] * 26  
        l, max_f, max_len = 0, 0, 0
        for r in range(len(s)):
            freq[self.char2idx(s[r])] += 1
            max_f = max(max_f, freq[self.char2idx(s[r])])

            while (r - l + 1) - max_f > k:
                freq[self.char2idx(s[l])] -= 1
                l += 1

            max_len = max(max_len, r - l + 1)
        return max_len
        



if __name__ == "__main__":
    # Include one-off tests here or debugging logic that can be run by running this file
    # e.g. print(solution.two_sum([1, 2, 3, 4], 3))
    solution = Solution()
