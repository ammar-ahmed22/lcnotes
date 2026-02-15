## Intuition
In a sorted array, comparing the target with the middle element tells us which half to search next. By repeatedly halving the search space, we find the target in logarithmic time.

## Implementation
Set left and right pointers to the array bounds. While left <= right, compute the midpoint. If the middle element equals the target, return its index. If the middle is less than the target, search the right half by setting left = mid + 1. Otherwise, search the left half by setting right = mid - 1.

## Edge-cases
The loop condition must be left <= right (not just <) to handle the case where the target is at the last remaining position when left equals right.

## Complexity
Time `O(log n)` as the search space halves each iteration. Space `O(1)` using only pointers.
