## Intuition
The reordering alternates between nodes from the start and end of the list. By reversing the second half and merging it with the first half, we can achieve this pattern in-place.

## Implementation
Three steps, each `O(n)`. First, find the midpoint using slow/fast pointers (fast starts at `head.next`). Second, reverse the second half starting at `slow.next` and break the link by setting `slow.next = None`. Third, merge by alternating: save next pointers for both halves, link `first.next` to `second`, link `second.next` to the saved first-next, then advance both pointers.

## Edge-cases
The algorithm handles odd and even length lists naturally. The midpoint calculation ensures the first half is equal or one longer than the second.

## Complexity
- Time: `O(n)` — three sequential O(n) passes
- Space: `O(1)` — all operations done in-place
