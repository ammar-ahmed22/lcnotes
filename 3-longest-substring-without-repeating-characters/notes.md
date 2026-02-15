## Intuition
A sliding window maintains the current substring. When a duplicate character enters from the right, shrink from the left until the duplicate is removed, ensuring all characters in the window are unique.

## Implementation
Use a set to track characters in the current window. Iterate with the right pointer. If the character at `r` is already in the set, remove characters from the left (incrementing `l`) until the duplicate is gone. Add the current character to the set and update the maximum length (`r - l + 1`).

## Edge-cases
The window size calculation is `r - l + 1` (inclusive on both ends). Empty strings return 0 naturally since the loop doesn't execute.

## Complexity
- Time: `O(n)` — each character added and removed from set at most once
- Space: `O(min(n, m))` — where m is the character set size (26 for lowercase letters)
