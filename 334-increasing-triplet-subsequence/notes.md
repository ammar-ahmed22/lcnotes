## Intuition
Track the smallest and second-smallest values seen so far. If we encounter a number larger than both, we've found an increasing triplet. The key insight is that even if `smallest` updates after `second_smallest` was set, the triplet still exists.

## Implementation
Initialize `smallest` and `second_smallest` to maximum values. Iterate through the array. If the current number is ≤ `smallest`, update `smallest`. Else if it's ≤ `second_smallest`, update `second_smallest`. Otherwise, we've found a number greater than both—return `True`. If the loop completes, return `False`.

## Edge-cases
Using ≤ (not <) handles duplicate values correctly. The algorithm works even when `smallest` updates to a value after `second_smallest` was set because a valid first element still existed when `second_smallest` was assigned.

## Complexity
- Time: `O(n)` — single pass through the array
- Space: `O(1)` — only two variables
