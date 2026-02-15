## Intuition
Without using division, we need another way to compute the product of all elements except the current one. The key observation is that for any index i, the answer is the product of all elements to its left multiplied by the product of all elements to its right.

## Implementation
Build two arrays: `prefix` where `prefix[i]` holds the product of all elements before index i, and `suffix` where `suffix[i]` holds the product of all elements after index i. Initialize `prefix[0] = 1` (nothing before the first element) and `suffix[n-1] = 1` (nothing after the last element). The answer at each index is simply `prefix[i] * suffix[i]`.

## Edge-cases
No special edge cases since the problem guarantees the product will fit in a 32-bit integer.

## Complexity
Time `O(n)` for three linear passes (prefix, suffix, and result). Space `O(n)` for the prefix and suffix arrays.
