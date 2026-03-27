## Intuition
We want to grab the two largest stones on every iteration.

## Implementation
To efficiently grab the two largest stones on every iteration, we can use a max heap.

Start by initializing our max heap. In Python, the standard heap is a min heap so we can negate each value to make it a max heap.

Next, we iterate while the max heap has at least 2 elements:
- Pop the two largest elements off the max heap, x and y (must be negated to get the actual values)
- If `x > y`, swap them
- If `x == y`, continue to the next iteration, no new stones added (both destroyed)
- Otherwise, add `y-x` to the heap (must be negated to maintain max heap property)

When the iteration completes, we either have 1 or 0 elements in the max heap, return the element or 0 if its empty.

## Edge-cases
Remember to negate when adding and negate when popping from the heap to ensure the max heap property is satisfied and we are comparing the actual stone values.

## Complexity
- Time: `O(n log n)`, we iterate over all stones once and in each iteration we are popping from the heap which is `O(log n)`.
- Space: `O(n)`, the max heap will start with all elements.
