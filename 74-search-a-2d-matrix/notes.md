## Intuition
The matrix is sorted both row-wise and column-wise, with each row's first element greater than the previous row's last element. This allows two binary searches: first find the correct row, then search within that row.

## Implementation
Binary search on rows using top and bottom pointers. A row is correct if the target falls between its first and last elements. Once found, perform standard binary search within that row. If the row search completes without finding a valid row, the target doesn't exist.

## Edge-cases
If the row containing the target range is found but the inner binary search fails, return False immediately—don't continue searching other rows.

## Complexity
Time `O(log m + log n)` for binary search on rows then columns. Space `O(1)` using only pointers.
