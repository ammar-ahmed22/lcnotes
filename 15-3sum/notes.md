## Intuition
Building on the two-pointer approach from Two Sum II, we can fix one number and use two pointers on the remaining sorted array to find pairs that sum to its negation. Sorting enables efficient duplicate skipping.

## Implementation
Sort the array first. For each number `nums[i]`, set up left and right pointers on the subarray to its right. If `l + r` equals the target (negation of `nums[i]`), we found a triplet. If the sum is too large, move right inward; if too small, move left outward. Continue searching even after finding a triplet.

## Edge-cases
Duplicates require careful handling. Skip duplicate values of `nums[i]` at the outer loop level. After finding a triplet, advance both `l` and `r` past any duplicates to avoid adding the same triplet multiple times.

## Complexity
- Time: `O(n²)` — sorting is `O(n log n)`, nested iteration is `O(n²)`
- Space: `O(1)` — excluding the output array
