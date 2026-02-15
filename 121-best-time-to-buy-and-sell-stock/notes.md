## Intuition
We need to find the maximum difference where the larger value comes after the smaller one. Track the minimum price seen so far and compute the potential profit at each step.

## Implementation
Use two pointers: buy (tracking the minimum price so far) and sell (current day). For each sell day, calculate profit. If positive, update max profit. If negative (current price is lower than buy price), move buy to the current position—we found a better buying opportunity.

## Edge-cases
If the array has one or zero elements, no transaction is possible—return 0.

## Complexity
Time `O(n)` for a single pass. Space `O(1)` using only pointers and a max tracker.
