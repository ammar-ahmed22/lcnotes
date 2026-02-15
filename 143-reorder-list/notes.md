## Intuition
The reordered list alternates between nodes from the start and nodes from the end. Achieve this by finding the middle, reversing the second half, and then interleaving the two halves.

## Implementation
Three steps: (1) Find the middle using slow/fast pointers, with fast starting at head.next for correct splitting. (2) Reverse the second half starting from slow.next, breaking the link by setting slow.next to None. (3) Merge by alternating nodes from both halves.

## Edge-cases
The merging loop continues while the second half has nodes. Since the first half may be one node longer (odd length lists), this works correctly.

## Complexity
Time `O(n)` for three sequential linear operations. Space `O(1)` modifying the list in place.
