## Intuition
In Reverse Polish Notation, operators come after their operands. A stack naturally handles this—operands are pushed, and when an operator appears, we pop the last two operands, apply the operation, and push the result.

## Implementation
Iterate through tokens. If the token is a number, push it onto the stack. If it's an operator, pop two values, apply the operation (with the second popped value as the left operand), and push the result. After processing all tokens, the stack contains one element: the answer.

## Edge-cases
For division and subtraction, operand order matters. The first pop gives the right operand, the second pop gives the left. Also, Python's `//` operator doesn't truncate toward zero for negative numbers—use `int(a / b)` instead.

## Complexity
Time `O(n)` for a single pass through tokens. Space `O(n)` for the stack.
