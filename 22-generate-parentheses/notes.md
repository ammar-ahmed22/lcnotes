## Intuition
Well-formed parentheses follow two rules: we can add an open bracket if we haven't used all n, and we can add a close bracket only if it wouldn't exceed the number of opens. Backtracking explores all valid combinations.

## Implementation
Use a recursive backtracking function tracking open count, closed count, and a stack for the current combination. Base case: when `open == closed == n`, we have a complete valid string—add it to results. Otherwise, if `open < n`, try adding an open bracket (recurse, then pop). If `closed < open`, try adding a close bracket (recurse, then pop).

## Edge-cases
No special edge cases. The constraints (`open < n` and `closed < open`) ensure only valid combinations are generated.

## Complexity
- Time: `O(4ⁿ/√n)` — the n-th Catalan number represents valid combinations
- Space: `O(n)` — recursion depth and stack for current combination
