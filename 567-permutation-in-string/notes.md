## Intuition
A permutation of s1 in s2 means a substring of s2 has the exact same character frequencies as s1. Slide a fixed-size window across s2 and check if frequencies match.

## Implementation
Use a single frequency array. First, increment for each character in s1, then decrement for the first `len(s1)` characters of s2. If all zeros, we found a match. Slide the window: increment the count of the character leaving (left), decrement the count of the character entering (right). Check for all zeros at each position.

## Edge-cases
Return early if `len(s1) > len(s2)`. Don't forget to check for a match after the final window position (after the loop exits).

## Complexity
- Time: `O(n)` — single pass through s2
- Space: `O(1)` — frequency array is fixed at 26 elements
