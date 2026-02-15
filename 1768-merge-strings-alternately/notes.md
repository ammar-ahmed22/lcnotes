## Intuition
The merge pattern alternates between strings: first character from word1, then word2, then word1, and so on. When one string is exhausted, append the remainder of the other.

## Implementation
Use two pointers (`i`, `j`) for each word and a counter `k` to track whose turn it is. While both pointers are in bounds, add from `word1` when `k` is even, from `word2` when odd, incrementing the respective pointer. After the main loop, append any remaining characters from whichever string isn't exhausted.

## Edge-cases
Strings of unequal length are handled by the trailing loops that append leftover characters. Empty strings work naturally—the main loop won't execute.

## Complexity
- Time: `O(n + m)` — each character processed once
- Space: `O(1)` — excluding the output string
