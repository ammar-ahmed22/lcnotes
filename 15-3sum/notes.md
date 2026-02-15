## Intuition
This extends the Two Sum II pattern. Sort the array first, then for each element, use two pointers to find pairs in the remaining array that sum to the negative of that element (making the total zero).

## Implementation
Sort the array. For each index i, set left pointer to i+1 and right pointer to the end. If the sum of all three equals zero, record the triplet. If the sum is too large, move right pointer left; if too small, move left pointer right.

## Edge-cases
To avoid duplicate triplets, skip over consecutive identical values for the outer loop index. Similarly, after finding a valid triplet, skip over duplicates for both left and right pointers before continuing the search.

## Complexity
Time `O(n^2)` for sorting plus the nested two-pointer search. Space `O(1)` excluding the output array.
