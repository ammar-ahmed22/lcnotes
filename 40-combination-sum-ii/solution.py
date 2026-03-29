from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = set()
        candidates.sort() # O(n log n)
        def recurse(i: int, curr: List[int], total: int):
            if total == target:
                res.add(tuple(curr))
                return
            if i >= len(candidates) or total > target:
                return
            
            # Case 1: Add the current number
            curr.append(candidates[i])
            recurse(i + 1, curr, total + candidates[i])

            # Case 2: Skip the current number and all duplicates
            curr.pop()

            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1

            recurse(i + 1, curr, total)

        recurse(0, [], 0)
        return [list(c) for c in res]



if __name__ == "__main__":
    # Include one-off tests here or debugging logic that can be run by running this file
    # e.g. print(solution.two_sum([1, 2, 3, 4], 3))
    solution = Solution()
