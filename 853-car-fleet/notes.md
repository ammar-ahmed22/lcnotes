## Intuition
Cars can only form fleets by catching up to slower cars ahead. Process cars from closest to target backward—if a car behind arrives at the same time or earlier than the car ahead, they form a fleet traveling at the slower car's speed.

## Implementation
Combine position and speed, then sort by position in descending order (closest to target first). Use a stack to track arrival times of fleet leaders. For each car, calculate its time to reach the target. If this time exceeds the stack's top (meaning it can't catch the fleet ahead), it becomes a new fleet leader—push it onto the stack.

## Edge-cases
Cars at the same position with different speeds should be handled by the sorting; the faster one would catch up instantly.

## Complexity
Time `O(n log n)` dominated by sorting. Space `O(n)` for the stack.
