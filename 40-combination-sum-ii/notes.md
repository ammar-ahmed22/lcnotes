## Intuition
For each number, we have two choices, use it or skip it. We also want to avoid using duplicates again.

## Implementation
We can solve this using recursing backtracking. Since we have two choices, we can recurse on both choices while traversing the array. In order to mitigate duplicates, we should also sort the array so that we can skip over all duplicates after using the first occurrence.

We initialize our result which will be a set to ensure there are no duplicate combinations.

The recursive function takes in the index, `i`, the current list of numbers, `curr`, in the combination and the `total`.
- If `total` equals `target`, we add `curr` as a tuple to the result
- If `i` exceeds the bounds or `total` is greater than target, we return early
- Our first choice is to the use the current number, we add it to the `curr` and recurse with `i + 1`, `curr` and the `total + candidates[i]`
- Our second choice is to skip the current number, so we pop it from `curr`
- We also want to skip over all duplicates at this point, so we iterate while `i + 1 < len(candidates) and candidates[i] = candidates[i + 1]` and increment `i`
- Then, we recurse with `i + 1`, `curr` and the `total` (unchanged because of skip)

Finally, we call the recursive function with `i = 0` and empty array for `curr` and `total = 0`. For the result, we create the result by making the tuples into arrays.

## Complexity
- Time: `O(n * 2^n)`, we iterate over each number and we have two recursive choices at each number
- Space: `O(n)`, the recursive call stack will only be, at most, `n`.
