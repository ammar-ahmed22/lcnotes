from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            curr = numbers[i]
            complement = target - curr
            l, r = i + 1, len(numbers) - 1
            while l <= r:
                m = (l + r) // 2
                if numbers[m] == complement:
                    return [i + 1, m + 1] # 1-based indexing
                elif numbers[m] < complement:
                    l = m + 1
                else:
                    r = m - 1


        print("should not get here, check testcases")
        return [0, 0]
        



if __name__ == "__main__":
    # Include one-off tests here or debugging logic that can be run by running this file
    # e.g. print(solution.two_sum([1, 2, 3, 4], 3))
    solution = Solution()
