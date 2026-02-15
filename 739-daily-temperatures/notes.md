## Intuition
A monotonic decreasing stack holds temperatures waiting for a warmer day. When a warmer temperature arrives, all cooler temperatures on the stack have found their answer.

## Implementation
Initialize the result array with zeros (default for days with no warmer future day). Use a stack storing (temperature, index) pairs. For each day, while the stack isn't empty and the current temperature is greater than the stack's top, pop and calculate the distance (`current_index - popped_index`). Store this in the result at the popped index. Push the current temperature and index.

## Edge-cases
Days that never see a warmer temperature remain 0 in the result (they're never popped from the stack).

## Complexity
- Time: `O(n)` — each element pushed and popped at most once
- Space: `O(n)` — stack in worst case (monotonically decreasing input)
