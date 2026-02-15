## Intuition
Expand the window until it contains all characters from t, then contract from the left to find the minimum valid window. Track required character frequencies and decrement as we include them in the window.

## Implementation
Build a frequency map of characters needed from t. Expand right, decrementing frequencies for matched characters. When all frequencies are <= 0 (all requirements met), the window is valid—record it if it's the smallest. Then shrink from the left, incrementing frequencies for removed characters, until the window becomes invalid again.

## Edge-cases
When expanding, update the frequency map after moving the pointer. When shrinking, update before moving. Initialize the result to empty string to distinguish "not found" from "found empty."

## Complexity
Time `O(m + n)` where m is the length of s and n is the length of t. Space `O(n)` for the frequency map.
