## Intuition
The matrix is sorted both row-wise and column-wise, with each row's first element greater than the previous row's last. First binary search to find the correct row, then binary search within that row.

## Implementation
Use binary search on rows: a row is valid if `target ≥ row[0]` and `target ≤ row[-1]`. Once the correct row is found, perform standard binary search within it. If the target isn't in the valid row, return `False` immediately.

## Edge-cases
If the row-level binary search completes without finding a valid row, return `False`—don't proceed to the column search.

## Complexity
- Time: `O(log m + log n)` — binary search on rows then columns
- Space: `O(1)` — only tracking pointers
