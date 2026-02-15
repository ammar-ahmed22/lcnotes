## Intuition
Since the digits are stored in reverse order, we can add them just like we would on paper—starting from the ones place and carrying over when the sum exceeds 9.

## Implementation
Create a dummy node for the result and maintain pointers for both input lists and the result. Track a carry value initialized to 0. While both lists have nodes, compute `p1.val + p2.val + carry`. The new digit is `total % 10` and the new carry is `total // 10`. Create a new node and advance all pointers. After the main loop, process any remaining nodes in either list with the same carry logic.

## Edge-cases
After processing both lists, the carry might still be non-zero (e.g., 99 + 1 = 100). Create a final node with the carry value if needed.

## Complexity
- Time: `O(n)` — traverse both lists once
- Space: `O(1)` — result list doesn't count toward space complexity
