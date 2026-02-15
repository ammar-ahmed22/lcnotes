## Intuition
Springs are most valuable for the largest height differences. Use sandbags first, and when you run out, retroactively convert the largest sandbag usage to a spring.

## Implementation
Use a max heap to track height differences. For each upward jump, subtract from sandbags and add the difference to the heap. If sandbags go negative and no springs remain, return the current index. Otherwise, use a spring by popping the largest jump from the heap and adding those sandbags back. Continue until the end.

## Edge-cases
Python's `heapq` is a min heap—negate values to simulate max heap behavior. Remember to negate again when popping.

## Complexity
- Time: `O(n log n)` — heap operations for each building
- Space: `O(n)` — heap stores jump sizes
