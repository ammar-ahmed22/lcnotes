## Intuition
Compress in-place by using a read pointer to count consecutive characters and a write pointer to build the compressed result. The write pointer always stays behind or at the read pointer.

## Implementation
Use three pointers: `l` (start of current group), `r` (scanner), and `k` (write position). Advance `r` while it matches `chars[l]` to count consecutive occurrences. Write the character at position `k`, then if the count (`r - l`) exceeds 1, write each digit of the count. Set `l = r` to start the next group. Return `k` as the new length.

## Edge-cases
Single occurrences don't get a count appended (only the character is written). Multi-digit counts (e.g., 12) need each digit written separately.

## Complexity
- Time: `O(n)` — each character read and written once
- Space: `O(1)` — compression done in-place
