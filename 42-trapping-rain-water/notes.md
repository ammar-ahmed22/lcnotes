## Intuition
Water at any position is bounded by the minimum of the maximum heights on its left and right. The two-pointer technique lets us compute this without precomputing all prefix/suffix maximums.

## Implementation
Use left and right pointers at opposite ends, tracking `maxL` (max height seen from left) and `maxR` (max height seen from right). Update these maxes on each iteration. If `maxL ≤ maxR`, we know the left side is the bottleneck—add `maxL - height[l]` to the answer and move left. Otherwise, the right side is the bottleneck—add `maxR - height[r]` and move right.

## Edge-cases
The algorithm handles flat terrain (no trapping) naturally since `max - height` will be zero. Empty arrays or single-element arrays trap no water.

## Complexity
- Time: `O(n)` — each element visited once
- Space: `O(1)` — only tracking pointers and two max values
