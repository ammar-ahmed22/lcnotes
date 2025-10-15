from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        map = {}
        for num in nums:
            map[num] = False

        max_sequence = 0
        for num in nums:
            is_sequence_start = num - 1 not in map
            if is_sequence_start and map[num] == False:
                map[num] = True # mark this sequence start as processed
                length = 0
                curr = num
                while curr in map:
                    curr += 1
                    length += 1
                max_sequence = max(max_sequence, length)


        return max_sequence
        



if __name__ == "__main__":
    # Include one-off tests here or debugging logic that can be run by running this file
    # e.g. print(solution.two_sum([1, 2, 3, 4], 3))
    solution = Solution()
