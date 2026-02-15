## Intuition
Treat the array as a linked list where each value points to the next index. Since there's a duplicate, following these "pointers" creates a cycle. The duplicate is where the cycle begins—finding the cycle's start gives us the answer.

## Implementation
Use Floyd's cycle detection in two phases. First, use fast and slow pointers until they meet—this confirms a cycle and places slow somewhere inside it. Second, start a new pointer at index 0 and advance both it and slow one step at a time. They'll meet at the cycle's start, which is the duplicate value.

## Edge-cases
The first phase only detects that a cycle exists; it doesn't find the start. The second phase is essential for locating the actual duplicate.

## Complexity
- Time: `O(n)` — both phases traverse at most n elements
- Space: `O(1)` — only using pointers
