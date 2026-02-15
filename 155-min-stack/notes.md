## Intuition
To retrieve the minimum in O(1), maintain a secondary stack that tracks the minimum value at each "level" of the main stack. The min stack's top always reflects the current minimum.

## Implementation
Use two stacks: a main stack for values and a min stack for minimums. On push, always add to the main stack. If the value is less than or equal to the current minimum (or the stack is empty), also push to the min stack. On pop, remove from the main stack, and if the popped value equals the min stack's top, also pop from the min stack.

## Edge-cases
Push to the min stack when the value equals the current minimum, not just when it's strictly less. This handles duplicate minimum values correctly.

## Complexity
Time `O(1)` for all operations. Space `O(n)` for both stacks in the worst case.
