## Intuition
Cars closer to the target may slow down cars behind them. If a car behind would arrive before the car ahead, they form a fleet. Process cars from closest to farthest, tracking fleet leaders.

## Implementation
Pair positions with speeds and sort by position in descending order (closest to target first). Use a stack to track arrival times of fleet leaders. For each car, calculate time to target. If this time exceeds the stack top's time, this car leads a new fleet—push its time. Otherwise, it joins an existing fleet (do nothing). The stack size is the number of fleets.

## Edge-cases
Cars at the same position with different speeds still follow the same logic—the slower one determines the fleet's speed.

## Complexity
- Time: `O(n log n)` — dominated by sorting
- Space: `O(n)` — stack and sorted array
