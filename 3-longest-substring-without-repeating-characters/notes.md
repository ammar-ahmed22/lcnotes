## Intuition
Use a sliding window that expands right and contracts left whenever we encounter a duplicate. The window always represents a valid substring without repeating characters.

## Implementation
Maintain a set of characters in the current window. Expand the window by moving the right pointer. If the new character already exists in the set, shrink from the left by removing characters until the duplicate is gone. Track the maximum window size throughout.

## Edge-cases
Window size is calculated as `r - l + 1` since both pointers are inclusive indices.

## Complexity
Time `O(n)` since each character is added and removed from the set at most once. Space `O(min(n, m))` where m is the character set size.
