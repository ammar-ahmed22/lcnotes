## Intuition
First find the rotation pivot (minimum element), which divides the array into two sorted subarrays. Then determine which subarray contains the target and perform standard binary search on it.

## Implementation
Use the Find Minimum in Rotated Sorted Array algorithm to locate the pivot index. Then check if the target falls in the left sorted portion (0 to pivot-1) or the right sorted portion (pivot to end). Perform binary search on the appropriate half.

## Edge-cases
When determining which half contains the target, compare against both the first element and the element before the pivot to correctly identify the range.

## Complexity
Time `O(log n)` for finding the pivot plus searching. Space `O(1)` using only pointers.
