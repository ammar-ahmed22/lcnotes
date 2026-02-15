## Intuition
For each bar, we want to find how far left and right it can extend as the shortest bar. A monotonic increasing stack helps—when we encounter a shorter bar, all taller bars on the stack can no longer extend right, so we calculate their areas.

## Implementation
Use a stack storing indices of bars in increasing height order. Iterate through the histogram plus one extra index (with height 0 to flush the stack). When the current height is less than the stack's top, pop and calculate area using the popped height and the width between the current index and the new stack top.

## Edge-cases
When the stack becomes empty after popping, the left boundary extends to index -1 (the popped bar spans from the start). Handle this by using -1 as the left index.

## Complexity
Time `O(n)` since each bar is pushed and popped at most once. Space `O(n)` for the stack.
