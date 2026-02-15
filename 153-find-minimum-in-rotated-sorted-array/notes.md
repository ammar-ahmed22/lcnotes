## Intuition
In a rotated sorted array, the minimum is the only element smaller than both its neighbors (the rotation pivot point). Binary search can find it by always moving toward the unsorted half.

## Implementation
Compare the middle element with the rightmost element. If mid > right, the minimum must be in the right half (that's where the rotation occurred). Otherwise, it's in the left half including mid. The minimum is found when an element is smaller than both neighbors.

## Edge-cases
Handle boundary conditions at index 0 and n-1 when checking neighbors. If mid is at these boundaries, only check the valid neighbor.

## Complexity
Time `O(log n)` for binary search. Space `O(1)` using only pointers.
