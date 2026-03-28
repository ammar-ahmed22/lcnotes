## Intuition
For each number, we have two choices; use it again or skip it.

## Implementation
Since we have two choices for each number and we want to explore all possible branches of this decision tree for each number, we can solve this using recursive back tracking.

We set up or recursive function to take in the index for the candidates, `i`, the current set of numbers, `curr`, and the current `total`. Our first base case is to check if the `total` is equal to the `target`, that means our `curr` is a set of numbers that adds up to the same so we addit to our result and return early. Our second base case is when `i` exceeds the bounds or if the total exceeds the target, this is now an invalid set or recursive parameters so we return early.

Now, for our two cases, the first case is to add the same number again. We add the number to `curr` and recurse with the same `i` and number added to the total. The second case is to skip the current number, so we pop from `curr` (because we just added it in the first case) and recurse with `i + 1` and the same `total`. We keep the total the same in the second case because adding to the total is handled by the first case, on the first time seeing a number it will be called with the first case of "using the same number again".

## Complexity
- Time: `O(2^(t/m))`, where `t` is the target and `m` is the smallest number in `candidates`. The worst-case is choosing the same number each time which will cause a recursion stack of `t/m` because each `m` will reduce `t` by `m`.
- Space: `O(t/m)`, recursion stack.
