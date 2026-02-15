## Intuition
Generate all valid combinations by building strings character by character, only adding characters that keep the string valid. We can add an open parenthesis if we haven't used all n, and a close parenthesis only if it doesn't exceed the number of opens.

## Implementation
Use backtracking with a recursive function tracking the count of open and close parentheses used. Base case: when both counts equal n, add the current string to results. Otherwise, try adding '(' if opens < n, then backtrack. Try adding ')' if closes < opens, then backtrack.

## Edge-cases
No special edge cases since the constraints ensure valid input (n >= 1).

## Complexity
Time is related to the n-th Catalan number: `O(4^n / sqrt(n))`. Space `O(n)` for the recursion depth and current string being built.
