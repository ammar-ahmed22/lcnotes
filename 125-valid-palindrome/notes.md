## Intuition
A palindrome reads the same forwards and backwards. Using two pointers starting from opposite ends and moving toward the center, we can verify this property in a single pass.

## Implementation
Initialize left pointer at the start and right pointer at the end. Move both toward the center, comparing characters. If they don't match, it's not a palindrome. Continue until the pointers meet or cross.

## Edge-cases
The input may contain non-alphanumeric characters and mixed case. Convert everything to lowercase and skip over any non-alphanumeric characters during traversal.

## Complexity
Time `O(n)` for a single pass through the string. Space `O(1)` using only two pointers.
