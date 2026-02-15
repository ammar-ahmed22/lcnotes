## Intuition
Track the smallest value and the smallest value that comes after it. If we ever find a third value larger than both, we have an increasing triplet.

## Implementation
Maintain two variables: `smallest` (minimum so far) and `second_smallest` (minimum value following some smaller value). For each number: if it's <= smallest, update smallest. Else if it's <= second_smallest, update second_smallest. Else, we found a value > second_smallest > smallest—return True.

## Edge-cases
The values don't need to be contiguous in the array. We're finding any increasing subsequence of length 3.

## Complexity
Time `O(n)` for a single pass. Space `O(1)` using only two tracking variables.
