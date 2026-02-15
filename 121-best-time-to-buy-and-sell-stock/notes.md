## Intuition
Since we must buy before we sell, we want to find the lowest price followed by the highest price after it. When we encounter a new low, that becomes our new potential buy point since any future profit would be better calculated from this lower price.

## Implementation
Use two pointers: `buy` starting at index 0 and `sell` at index 1. Iterate while `sell` is in bounds. Calculate the current profit—if positive, update the max profit. If the profit is negative or zero, we've found a lower price, so move `buy` to the current `sell` position. Always increment `sell` to continue scanning forward.

## Edge-cases
If the array has fewer than 2 elements, no transaction is possible, so return 0 immediately.

## Complexity
- Time: `O(n)` — single pass through the array
- Space: `O(1)` — only tracking pointers and max profit
