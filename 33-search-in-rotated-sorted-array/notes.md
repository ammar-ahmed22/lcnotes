## Intuition
First find where the array was rotated (the pivot/minimum element), which splits the array into two sorted subarrays. Then determine which subarray contains the target and perform a standard binary search on it.

## Implementation
First, binary search to find the pivot index using the "minimum in rotated sorted array" approach (where both neighbors are larger, or we're at a boundary). Then check if the target falls in the range from index 0 to pivot-1 (the "left" sorted portion) or from pivot to end (the "right" sorted portion). Binary search the appropriate half.

## Edge-cases
When determining which half to search, check if target falls within `nums[0]` to `nums[pivot-1]`. Handle the case where pivot is 0 (array wasn't rotated or rotated n times).

## Complexity
- Time: `O(log n)` — two binary searches
- Space: `O(1)` — only tracking pointers
