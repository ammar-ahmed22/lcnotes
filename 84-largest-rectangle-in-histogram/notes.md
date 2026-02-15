## Intuition
A monotonic increasing stack tracks bars that could be the height of a rectangle extending to the right. When a shorter bar appears, taller bars can no longer extend further—we calculate their maximum rectangle and pop them.

## Implementation
Iterate through bars (plus a sentinel height of 0 to flush the stack). Maintain a stack of indices in increasing height order. When the current bar is shorter than the stack's top, pop and calculate the area using that bar's height. The width extends from the new stack top (or -1 if empty) to the current index. Track the maximum area.

## Edge-cases
When the stack is empty after popping, the left boundary is -1 (the bar extends to the start). The sentinel value at the end ensures all remaining bars are processed.

## Complexity
- Time: `O(n)` — each bar pushed and popped at most once
- Space: `O(n)` — stack in worst case (ascending heights)
