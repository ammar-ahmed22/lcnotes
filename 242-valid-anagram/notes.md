## Intuition
Two strings are anagrams if they contain the same characters with the same frequencies. A fixed-size frequency array can track character counts efficiently.

## Implementation
Create a 26-element array for lowercase letters. Iterate through string `s`, incrementing the count at each character's index (`ord(char) - ord('a')`). Then iterate through `t`, decrementing the counts. If the strings are anagrams, all counts will be zero at the end.

## Edge-cases
Strings of different lengths cannot be anagrams. This is implicitly checked—the frequency array won't be all zeros if lengths differ.

## Complexity
- Time: `O(n)` — two passes through the strings
- Space: `O(1)` — frequency array is fixed at 26 elements
