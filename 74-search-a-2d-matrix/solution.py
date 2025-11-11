from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        t, b = 0, len(matrix) - 1 # top and bottom
        while t <= b:
            c = (t + b) // 2 # center row
            if target >= matrix[c][0] and target <= matrix[c][-1]:
                l, r = 0, len(matrix[c]) - 1
                while l <= r:
                    m = (l + r) // 2
                    if matrix[c][m] == target:
                        return True
                    elif matrix[c][m] < target:
                        l = m + 1
                    else:
                        r = m - 1
                return False # row that should contain it doesn't
            elif target < matrix[c][0]:
                # row is above, move b
                b = c - 1
            else:
                # row is below, move t
                t = c + 1
        return False
        



if __name__ == "__main__":
    # Include one-off tests here or debugging logic that can be run by running this file
    # e.g. print(solution.two_sum([1, 2, 3, 4], 3))
    solution = Solution()
