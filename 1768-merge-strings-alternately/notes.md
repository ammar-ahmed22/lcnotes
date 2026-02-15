## Intuition
Alternate between the two strings, taking one character at a time from each. When one string is exhausted, append the remainder of the other.

## Implementation
Use two pointers (i for word1, j for word2) and a counter k. While both strings have characters remaining, add from word1 when k is even, from word2 when k is odd. After one string is exhausted, append any remaining characters from the other.

## Edge-cases
Strings may have different lengths. The remaining characters from the longer string are simply appended at the end.

## Complexity
Time `O(n + m)` touching each character once. Space `O(1)` excluding the output string.
