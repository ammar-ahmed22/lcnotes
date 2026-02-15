## Intuition
In a rotated sorted array, the minimum element is the pivot point where the rotation occurred. It's the only element where both neighbors are larger (or it's at a boundary).

## Implementation
Use binary search. The stop condition is when the element before and after `mid` are both greater (or `mid` is at a boundary). To decide which half to search, compare `nums[mid]` with `nums[r]`—if `mid` is larger, the minimum is in the right half; otherwise, it's in the left half.

## Edge-cases
Boundary checks are essential. When `mid` is 0 or `n-1`, we can't compare with neighbors, so include these cases in the stop condition to avoid index out of bounds.

## Complexity
- Time: `O(log n)` — binary search halves the range each iteration
- Space: `O(1)` — only tracking pointers
