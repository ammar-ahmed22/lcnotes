## Intuition
Brackets must be closed in the reverse order they were opened (LIFO). A stack naturally models this—push opening brackets and pop when we see their matching closing brackets.

## Implementation
Create a map from opening to closing brackets. When encountering an opening bracket, push its expected closing bracket onto the stack. When encountering a closing bracket, check if it matches the stack's top. If it matches, pop and continue; if not, the string is invalid.

## Edge-cases
Check for two conditions: if a closing bracket appears when the stack is empty (no matching opener), and if the stack is non-empty after processing (unclosed brackets remain).

## Complexity
Time `O(n)` for a single pass through the string. Space `O(n)` for the stack in the worst case of all opening brackets.
