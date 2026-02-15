## Intuition
Add digits from both lists like pencil-and-paper arithmetic—sum corresponding digits plus any carry, keep the ones digit, carry the tens digit to the next position.

## Implementation
Use a dummy node for the result. Iterate while either list has nodes or there's a carry. For each position, sum the available values plus carry. The new digit is sum % 10, and the new carry is sum // 10. After both lists are exhausted, if carry remains, add one final node.

## Edge-cases
Don't forget to handle remaining carry after processing both lists. Lists of different lengths are handled naturally by treating exhausted lists as contributing zero.

## Complexity
Time `O(max(m, n))` where m and n are list lengths. Space `O(1)` excluding the result list.
