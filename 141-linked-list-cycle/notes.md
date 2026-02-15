## Intuition
Floyd's cycle detection: use two pointers moving at different speeds. If there's a cycle, the fast pointer will eventually lap the slow pointer and they'll meet. If no cycle, fast will reach the end.

## Implementation
Initialize both slow and fast pointers at the head. Move slow by one step and fast by two steps each iteration. If they ever point to the same node, a cycle exists. If fast reaches None or fast.next is None, there's no cycle.

## Edge-cases
Check both fast and fast.next before advancing to avoid null pointer errors when the list is short or has no cycle.

## Complexity
Time `O(n)` since fast pointer moves twice as fast and will either exit or catch up within n steps. Space `O(1)` using only two pointers.
