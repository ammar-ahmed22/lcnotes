## Intuition
Reverse Polish Notation places operators after their operands. A stack naturally handles this—operands accumulate until an operator consumes them, and intermediate results stay on the stack for future operations.

## Implementation
Iterate through tokens. If it's a number, push to stack. If it's an operator, pop the top two values, apply the operation, and push the result back. The final answer is the single value remaining on the stack.

## Edge-cases
Python's integer division `//` rounds toward negative infinity, not toward zero. Use `int(b / a)` for truncation toward zero. Also remember operand order matters for subtraction and division—the second popped value is the left operand (`b - a`, `int(b / a)`).

## Complexity
- Time: `O(n)` — single pass through tokens
- Space: `O(n)` — stack holds intermediate values
