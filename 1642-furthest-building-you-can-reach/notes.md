## Intuition
Ladders can cover any height difference, so they're most valuable for the largest jumps. By greedily using bricks first and retroactively converting the largest brick usage to a ladder when we run out, we maximize our reach.

## Implementation
Use a max heap to track jump sizes. For each positive height difference, assume we use bricks and add the difference to the heap. If bricks go negative, we need a ladder—if none remain, return the current index. Otherwise, use a ladder by popping the largest jump from the heap and adding those bricks back. If we complete the iteration, return the last index.

## Edge-cases
Python's `heapq` is a min heap, so negate values to simulate a max heap. Remember to negate again when popping.

## Complexity
- Time: `O(n log n)` — heap operations for each building
- Space: `O(n)` — heap stores up to n jumps
