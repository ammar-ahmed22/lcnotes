## Intuition
In a sorted array, we can eliminate half the search space with each comparison. If the middle element is too small, the target must be in the right half; if too large, it's in the left half.

## Implementation
Maintain left and right pointers. While `l ≤ r`, calculate the midpoint. If `nums[mid]` equals the target, return `mid`. If it's less than the target, search the right half by setting `l = mid + 1`. If greater, search the left half by setting `r = mid - 1`. If the loop exits, the target doesn't exist—return -1.

## Edge-cases
The condition must be `l ≤ r` (not `l < r`) to handle the case where the target is the only remaining element when `l == r`.

## Complexity
- Time: `O(log n)` — halve the search space each iteration
- Space: `O(1)` — only tracking pointers
