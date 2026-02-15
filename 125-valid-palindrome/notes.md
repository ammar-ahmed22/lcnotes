## Intuition
A palindrome reads the same forwards and backwards. By comparing characters from both ends moving toward the center, we can verify this property in a single pass.

## Implementation
Use left and right pointers starting at opposite ends. Iterate while `l < r`, comparing characters at each position. If they don't match, return `False` immediately. If the loop completes, the string is a valid palindrome.

## Edge-cases
The input may contain non-alphanumeric characters and mixed case. Convert the string to lowercase first, then skip over any non-alphanumeric characters during traversal by incrementing/decrementing the pointers without comparing.

## Complexity
- Time: `O(n)` — each character visited at most once
- Space: `O(1)` — only using pointers
