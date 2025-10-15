class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq = [0] * 26

        for char in s:
            freq[ord(char) - ord('a')] += 1

        for char in t:
            freq[ord(char) - ord('a')] -= 1

        return all(f == 0 for f in freq)
        



if __name__ == "__main__":
    # Include one-off tests here or debugging logic that can be run by running this file
    # e.g. print(solution.two_sum([1, 2, 3, 4], 3))
    solution = Solution()
