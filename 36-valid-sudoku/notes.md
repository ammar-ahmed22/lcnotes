## Intuition
A valid Sudoku board must have no duplicate digits in any row, column, or 3x3 subbox. We need to validate all three constraints independently.

## Implementation
Use a hashmap to track seen digits for each constraint. Iterate through rows checking for duplicates, then columns, then each 3x3 subbox. For subboxes, use nested loops with the outer loops selecting which box (0-2 for both row and column) and inner loops iterating within that box.

## Edge-cases
The tricky part is indexing into 3x3 subboxes. With box indices `brow` and `bcol` (0-2) and local indices `row` and `col` (0-2), access the cell at `board[3 * brow + row][3 * bcol + col]`.

## Complexity
Time `O(1)` since the board is always 9x9. Space `O(1)` since the hashmaps hold at most 9 elements each.
