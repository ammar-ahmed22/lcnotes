## Intuition
Brackets must close in the reverse order they were opened. A stack naturally enforces this LIFO property—each closing bracket should match the most recently opened one.

## Implementation
Use a map from opening to closing brackets. When encountering an opening bracket, push its expected closing bracket to the stack. When encountering a closing bracket, check if it matches the stack top—if so, pop and continue; if not (or stack is empty), return `False`.

## Edge-cases
Two important checks: the stack must be empty at the end (no unclosed brackets), and encountering a closing bracket when the stack is empty means there's no matching opener.

## Complexity
- Time: `O(n)` — single pass through the string
- Space: `O(n)` — stack can hold up to n/2 brackets
