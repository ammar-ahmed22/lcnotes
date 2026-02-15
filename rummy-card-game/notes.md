## Intuition
Rummy melds are either sets (same rank, different suits) or runs (consecutive ranks, same suit). Group cards by rank and suit separately, then generate all valid combinations.

## Implementation
Build two hashmaps: one grouping cards by rank, another by suit. For sets, find ranks with 3+ cards and generate all combinations of size 3, 4, etc. For runs, sort each suit's cards by rank, find consecutive segments, and generate all windows of size 3+ within each segment.

## Edge-cases
After processing consecutive cards, there may be a final segment that didn't trigger the flush logic—handle it after the loop.

## Complexity
- Time: `O(n²)` — generating combinations; acceptable for small card counts
- Space: `O(n²)` — storing all possible melds
