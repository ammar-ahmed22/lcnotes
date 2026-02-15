## Intuition
Track required character frequencies from `t`. A window is valid when all frequencies are satisfied (≤ 0 after decrementing). Expand the window to find valid substrings, then shrink to find the minimum.

## Implementation
Build a frequency map of characters in `t`. Process the first window of size `len(t)`, decrementing counts. Slide the window: when valid (all counts ≤ 0), update the minimum and shrink from the left. When invalid or at minimum size, expand from the right. Update the frequency map appropriately when characters enter or leave the window.

## Edge-cases
Update order matters: when expanding right, decrement AFTER moving. When shrinking left, increment BEFORE moving. Handle the case where no valid window exists (return empty string).

## Complexity
- Time: `O(m)` — sliding window across s
- Space: `O(n)` — frequency map for characters in t
