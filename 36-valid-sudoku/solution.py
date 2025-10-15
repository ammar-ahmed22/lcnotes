from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # Check rows
        for row in range(len(board)):
            map = {}
            for col in range(len(board[row])):
                if board[row][col] == ".":
                    continue
                if board[row][col] in map:
                    return False
                map[board[row][col]] = True

        # Check cols
        for col in range(len(board)):
            map = {}
            for row in range(len(board[col])):
                if board[row][col] == ".":
                    continue
                if board[row][col] in map:
                    return False
                map[board[row][col]] = True

        # Check sub boxes
        for brow in range(3):
            for bcol in range(3):
                map = {}
                for row in range(3):
                    for col in range(3):
                        if board[3 * brow + row][3 * bcol + col] == ".":
                            continue
                        if board[3 * brow + row][3 * bcol + col] in map:
                            return False
                        map[board[3 * brow + row][3 * bcol + col]] = True
        return True
        



if __name__ == "__main__":
    # Include one-off tests here or debugging logic that can be run by running this file
    # e.g. print(solution.two_sum([1, 2, 3, 4], 3))
    solution = Solution()
