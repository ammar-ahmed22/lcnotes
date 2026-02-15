## Intuition
Water at any position is bounded by the minimum of the maximum heights to its left and right, minus its own height. We can compute this efficiently using two pointers tracking the max heights seen from each direction.

## Implementation
Use left and right pointers starting at the ends. Track maxL (max height seen from left) and maxR (max height seen from right). If maxL <= maxR, the left side is the bottleneck—calculate water at left pointer using maxL, then move left. Otherwise, calculate at right pointer using maxR and move right.

## Edge-cases
No water can be trapped at the first and last positions since there's no wall on one side.

## Complexity
Time `O(n)` for a single pass. Space `O(1)` using only pointers and max trackers.
