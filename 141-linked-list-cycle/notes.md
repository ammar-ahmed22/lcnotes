## Intuition
Floyd's cycle detection uses two pointers moving at different speeds. If there's a cycle, the fast pointer will eventually lap the slow pointer and they'll meet. If there's no cycle, the fast pointer will reach the end.

## Implementation
Initialize both `slow` and `fast` pointers to the head. Iterate while `fast` and `fast.next` exist. Move `slow` by one step and `fast` by two steps. After each move, check if they're equal—if so, a cycle exists. If the loop terminates (fast reaches null), there's no cycle.

## Edge-cases
The iteration condition `fast and fast.next` naturally handles empty lists and lists with a single node.

## Complexity
- Time: `O(n)` — fast pointer traverses at most 2n nodes before meeting slow
- Space: `O(1)` — only two pointers
