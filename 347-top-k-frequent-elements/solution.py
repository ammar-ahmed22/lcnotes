from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = {}
        for num in nums:
            if num in map:
                map[num] += 1
            else:
                map[num] = 1

        freq_table = [[] for _ in range(len(nums) + 1)]
        for num in map:
            freq = map[num]
            freq_table[freq].append(num)

        ans = []
        for i in range(len(freq_table) - 1, -1, -1):
            for j in range(len(freq_table[i]) - 1, -1, -1):
                ans.append(freq_table[i][j])
                if len(ans) == k:
                    return ans


        return ans



if __name__ == "__main__":
    # Include one-off tests here or debugging logic that can be run by running this file
    # e.g. print(solution.two_sum([1, 2, 3, 4], 3))
    solution = Solution()
