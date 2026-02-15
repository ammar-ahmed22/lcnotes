## Intuition
For each day, we need to find the next warmer day. A monotonic decreasing stack helps—when we find a warmer temperature, it's warmer than all temperatures currently on the stack, so we can pop and compute distances.

## Implementation
Initialize a result array with zeros (default for days with no warmer future day). Use a stack storing (temperature, index) pairs. For each day, while the stack is non-empty and the current temperature is warmer than the stack's top, pop and record the distance in the result. Then push the current day onto the stack.

## Edge-cases
Days remaining on the stack after processing have no warmer future day, which is correctly represented by the initialized zeros.

## Complexity
Time `O(n)` since each element is pushed and popped at most once. Space `O(n)` for the stack.
