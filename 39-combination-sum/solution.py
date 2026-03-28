from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def recurse(i: int, curr: List[int], total: int):
            if total == target:
                res.append(curr.copy())
                return
            if i >= len(candidates) or total > target:
                return

            curr.append(candidates[i])

            # Case 1: add the current number again (duplicates allowed)
            recurse(i, curr, total + candidates[i])

            # Case 2: Skip the current number
            curr.pop()
            recurse(i + 1, curr, total)


        recurse(0, [], 0)
        return res



if __name__ == "__main__":
    # Include one-off tests here or debugging logic that can be run by running this file
    # e.g. print(solution.two_sum([1, 2, 3, 4], 3))
    solution = Solution()
