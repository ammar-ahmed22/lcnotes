## Intuition
At each element, there are exactly two choices: include it in the current subset or skip it. Backtracking explores both branches at every position, naturally generating all 2^n subsets.

## Implementation
Use a recursive `recurse(i)` with a shared `subset` list and `res` list. Base case: when `i >= len(nums)`, append a copy of `subset` to `res`. Otherwise, add `nums[i]` to `subset` and recurse (include branch), then pop it and recurse again (exclude branch)—both advancing to `i + 1`.

## Edge-cases
The empty set is handled naturally—it's added when all elements take the exclude branch. No duplicate handling is needed since the problem guarantees unique elements.

## Complexity
- Time: `O(n  2^n)`: `2^n` subsets, each taking up to `O(n)` to copy
- Space: `O(n)`: recursion depth and the current subset list, excluding output
