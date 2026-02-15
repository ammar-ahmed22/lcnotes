## Intuition
The product of all elements except self is equivalent to (product of all elements before i) × (product of all elements after i). We can precompute these prefix and suffix products.

## Implementation
Build a `prefix` array where `prefix[i]` is the product of all elements before index `i`. Initialize `prefix[0] = 1` (nothing before it), then `prefix[i] = nums[i-1] * prefix[i-1]`. Similarly, build a `suffix` array from right to left where `suffix[i]` is the product of all elements after index `i`. The answer at each index is `prefix[i] * suffix[i]`.

## Edge-cases
The edge indices are handled by initializing prefix and suffix with 1s. No division is needed, so zeros in the array don't cause issues.

## Complexity
- Time: `O(n)` — three linear passes
- Space: `O(n)` — prefix and suffix arrays (can be optimized to O(1) by computing on the fly)
