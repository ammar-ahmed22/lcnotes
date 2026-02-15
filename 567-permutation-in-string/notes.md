## Intuition
A permutation of s1 has exactly the same character frequencies as s1. Slide a fixed-size window (length of s1) across s2 and check if the window's frequency matches s1's frequency.

## Implementation
Build a frequency map from s1. Slide a window of the same size across s2: subtract entering characters and add leaving characters to the map. When all frequencies are zero, we've found a permutation. Use a single map—increment for s1 chars, decrement for s2 window chars.

## Edge-cases
If s1 is longer than s2, no permutation can exist—return False immediately. Also check the final window position after the loop ends.

## Complexity
Time `O(n)` where n is the length of s2. Space `O(1)` since the frequency array is always 26 elements.
