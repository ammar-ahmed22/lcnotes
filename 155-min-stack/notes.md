## Intuition
To support `O(1)` minimum retrieval, we need to track minimums as they change. A second stack that only stores values when they become the new minimum (or equal to it) maintains this information.

## Implementation
Maintain two stacks: the main stack and a min stack. On `push`, always add to the main stack; if the value is less than or equal to the current minimum (or min stack is empty), also push to min stack. On `pop`, if the popped value equals the min stack top, pop from min stack too. `getMin` returns the top of min stack. `top` returns the main stack top.

## Edge-cases
Push to min stack when value equals the current min (not just less than) to handle duplicate minimums correctly.

## Complexity
- Time: `O(1)` — all operations are constant time
- Space: `O(n)` — both stacks can grow to n elements
