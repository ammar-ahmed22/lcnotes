class Solution:
    def char2idx(self, c: str) -> int:
        return ord(c) - ord('a')

    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        freq = [0] * 26
        for c in s1:
            freq[self.char2idx(c)] += 1

        for i in range(len(s1)):
            freq[self.char2idx(s2[i])] -= 1

        l, r = 0, len(s1)

        while r < len(s2):
            if all(x == 0 for x in freq):
                return True
            
            # Leaving window
            freq[self.char2idx(s2[l])] += 1
            # Entering window
            freq[self.char2idx(s2[r])] -= 1
            l += 1
            r += 1


        return all(x == 0 for x in freq)
        



if __name__ == "__main__":
    # Include one-off tests here or debugging logic that can be run by running this file
    # e.g. print(solution.two_sum([1, 2, 3, 4], 3))
    solution = Solution()
