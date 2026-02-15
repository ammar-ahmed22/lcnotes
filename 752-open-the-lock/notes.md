## Intuition
Model the lock as a graph where each 4-digit combination is a node, connected to 8 neighbors (each wheel can turn up or down). BFS finds the minimum turns from "0000" to the target.

## Implementation
Generate neighbors by incrementing or decrementing each digit (mod 10). BFS from "0000": skip deadends and visited states, return turn count when reaching target. Track visited states to avoid cycles.

## Edge-cases
Check if "0000" is in deadends—if so, return -1 immediately. Also handle the case where start equals target.

## Complexity
Time `O(10^4 * 8)` for BFS across all possible combinations. Space `O(10^4)` for the visited set and queue.
