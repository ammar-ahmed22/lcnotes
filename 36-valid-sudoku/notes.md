## Intuition
A valid Sudoku has no duplicates in any row, column, or 3×3 subbox. We need to verify all three constraints independently.

## Implementation
Use hashmaps to track seen values. First, iterate through each row checking for duplicates. Then iterate through each column. Finally, check each of the nine 3×3 subboxes. Skip empty cells (".") during all checks.

## Edge-cases
The 3×3 subbox indexing is tricky. Use four nested loops: `box_row (0-2)`, `box_col (0-2)`, `row (0-2)`, `col (0-2)`. Access cells with `board[3 * box_row + row][3 * box_col + col]`.

## Complexity
- Time: `O(1)` — board is always 9×9, so effectively constant
- Space: `O(1)` — hashmaps hold at most 9 elements each
