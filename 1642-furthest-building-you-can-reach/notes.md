## Intuition
Ladders should be reserved for the largest climbs since they handle any height. Use bricks first, and when bricks run out, retroactively convert the largest brick usage to a ladder.

## Implementation
Track all climbs in a max heap. For each climb, use bricks and push the climb to the heap. If bricks go negative, use a ladder instead: pop the largest climb from the heap and add those bricks back. If no ladders remain when needed, return the current index.

## Edge-cases
Downward moves (negative differences) are free—skip them. Return the last index if we successfully traverse the entire array.

## Complexity
Time `O(n log n)` for heap operations. Space `O(n)` for the heap.
